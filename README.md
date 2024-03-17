# Projeto de Classificação de Tipos de Pokémon

## Participantes: Elison Mélo, José Henrique, Pedro Luiz, Rônald Macário

### Introdução

Este relatório apresenta o desenvolvimento do projeto de Inteligência Artificial, que consiste em aplicar pelo menos três algoritmos a um problema de classificação ou regressão. O objetivo é analisar e comparar o desempenho dos algoritmos e selecionar um modelo para implantação.

### Problema

O problema selecionado para este projeto é responder à seguinte pergunta: é possível descobrir o tipo específico de um pokémon a partir de suas características básicas?

### Desenvolvimento do Projeto

#### Etapas

**Definição do Problema**

O objetivo desta etapa é entender o problema e definir claramente os objetivos do projeto. O problema escolhido consiste em determinar se é possível descobrir o tipo específico de um pokémon a partir de suas características básicas.

Para isso, serão utilizados algoritmos de classificação em machine learning, que serão treinados com um conjunto de dados contendo informações sobre as características dos pokémons. O sucesso do projeto será medido pela capacidade dos algoritmos em identificar corretamente o tipo de pokémon com base nas características fornecidas.

**Coleta de Dados**

Os dados foram coletados de três fontes diferentes:

1. Dados primários - esses dados trazem informações sobre características básicas dos pokémons, como peso, velocidade, ataque, defesa, etc. Esses dados vieram de um dataset do Kaggle: [The Complete Pokemon Dataset](https://www.kaggle.com/datasets/rounakbanik/pokemon)

2. Dados secundários - esses dados trazem informações sobre as três cores básicas dos pokémons e foram retirados de um site de paletas de cores de pokémons através de data scraping: [Pokémon Palette](https://pokemonpalette.com/)

3. Dados terciários - esses dados trazem dados classificadores sobre os pokémons que são baseados em animais/plantas através de data scraping: [Pokémon designed after animals or plants](https://bulbapedia.bulbagarden.net/wiki/User:Reshi643/Pok%C3%A9mon_designed_after_animals_or_plants)

**Análise Exploratória**

Devido à falta de informação no dataset principal, foi necessário obter mais dados relacionados aos Pokémons. Embora as informações que tínhamos fossem valiosas para a classificação dos Pokémons, não eram suficientes para o modelo distingui-los satisfatoriamente. O processo criativo para criar um Pokémon é complexo, e encontrar padrões nele não é uma tarefa trivial. No entanto, observamos que era possível encontrar padrões relacionados às cores e às inspirações nos seres vivos da realidade. Essas informações foram utilizadas no pré-processamento dos dados, juntamente com técnicas como label encoding e one-hot encoding.

**Pré-processamento**

Foram mescladas as tabelas de dados primários, secundários e terciários. As colunas das cores do Pokémon tinham valores hexadecimais e estavam no formato de string, então foram transformadas para o formato RGB que possui valores de 0 a 255. Três colunas para cada cor foram criadas ('red 1', 'green 1', 'blue 1'... 'red 3', 'green 3', 'blue 3'), e as colunas antigas foram excluídas. A coluna “capture_rate” foi convertida para o tipo numérico. Inicialmente queríamos que o modelo conseguisse detectar tanto o tipo primário quanto o secundário, porém, a complexidade da tarefa aumentaria muito, seriam 153 classes diferentes. Tentamos fazer one-hot encoding da tabela dos tipos 1 e 2, porém isso fez com que tivéssemos duas colunas de respostas. Os modelos que tínhamos à nossa disposição não suportam múltiplos outputs. Juntamos as colunas do tipo 1 e do tipo 2 para que a resposta fosse unificada. Apesar da tentativa, retornamos à questão de existirem muitas classes, decidimos por dropar a coluna do tipo 2 e assim tínhamos 18 classes no total. Para a coluna dos “tipos” utilizamos label encoding para atribuir valores numéricos aos valores categóricos dos tipos. Para a coluna “super_type” (Grupo animal) e “specific_type” (Classe ou família animal) utilizamos one-hot encoding. Então dropamos as colunas de nomes ou daquelas que se mostraram irrelevantes na visualização de dados para evitar ruído para o modelo ('height_m', 'name', 'japanese_name', 'pokedex_number', 'percentage_male', 'classfication', 'base_egg_steps', 'base_happiness', 'abilities', 'experience_growth', 'defense', 'base_total', 'speed'). Existiam valores nulos na coluna “capture_rate”, utilizamos a mediana desse valor para preencher. Dropamos a coluna de multiplicadores dos pokémons, isso acabava dando a resposta para o modelo. Tentamos utilizar o k-means e aproveitar os labels produzidos para substituir as colunas com os valores RGB, porém, devido a natureza não supervisionada do k-means e principalmente nossa base de dados, centros muito próximos foram produzidos e prejudicou a precisão do modelo. Como alternativa, tentamos estabelecer os centros de 7 cores e calculamos a distância euclidiana das cores do Pokémon e consideramos a cor do Pokémon aquela que está mais próxima, não obtivemos sucesso também, o modelo teve uma precisão tão baixa quanto a tentativa do k-means. Consideramos estabelecer o alcance das 7 cores, se a cor do pokémon estiver dentro daquele alcance, a cor do pokémon será rotulada como aquela, porém, não colocamos a ideia em prática. Por fim, passamos todas as colunas pela função “to_numeric” e normalizamos o dataframe.

**Modelagem**

Nesta etapa, foram selecionados três algoritmos de classificação considerando sua compatibilidade com o problema proposto de identificar o tipo específico de um pokémon a partir de suas características básicas. Os algoritmos escolhidos foram:

1. **Multi-Layer Perceptron (MLP)**:
   - O MLP foi selecionado devido à sua capacidade de aprender padrões complexos nos dados.
   - Este algoritmo é conhecido por sua eficácia em problemas de classificação com conjuntos de dados de médio a grande porte.

2. **K-Nearest Neighbors (K

NN)**:
   - O KNN foi escolhido por sua simplicidade e capacidade de classificar novos pontos de dados com base na proximidade com os pontos de dados existentes.
   - É um algoritmo não paramétrico que não faz suposições sobre a distribuição dos dados.

3. **Árvore de Decisão (Decision Tree)**:
   - A Árvore de Decisão foi selecionada devido à sua interpretabilidade e capacidade de lidar com conjuntos de dados com variáveis categóricas.
   - Este algoritmo é capaz de capturar relações não lineares entre os recursos e os rótulos.

#### Justificativas

**Métrica de Avaliação**

A métrica escolhida para avaliar o desempenho dos modelos foi a acurácia. A escolha baseia-se na sua capacidade de fornecer uma medida direta da proporção de predições corretas em relação ao total de predições realizadas.

Nesse contexto, a acurácia é uma métrica adequada, pois permite uma avaliação simples e intuitiva do desempenho dos modelos. Além disso, como o objetivo do projeto é determinar se é possível descobrir o tipo específico de um pokémon a partir de suas características básicas, a acurácia fornece uma medida clara de quão bem os modelos estão realizando essa tarefa, sendo uma escolha natural para a avaliação dos resultados.

### Desempenho dos Algoritmos

Os algoritmos foram avaliados utilizando o conjunto de treinamento e teste. A tabela a seguir mostra os resultados:

| Algoritmo      | Acurácia Treino | Acurácia Teste |
|----------------|-----------------|----------------|
| MLP            | 41,14%          | 41,94%         |
| KNN            | 42,55%          | 53,01%         |
| Decision Tree  | 99,70%          | 44,58%         |

### Modelo Selecionado

O modelo escolhido para ser colocado em produção foi o K-Nearest Neighbors (KNN). A escolha foi feita com base na métrica estatística de previsão do modelo, visto que este foi o modelo com a melhor capacidade de prever o tipo do pokémon, tendo uma acurácia de 53,01% para os dados de teste.

### Conclusão

O projeto de Inteligência Artificial apresentado teve como objetivo principal explorar a capacidade de diferentes algoritmos de classificação em identificar o tipo específico de um pokémon a partir de suas características básicas. Através de um processo que envolveu a coleta e pré-processamento de dados, análise exploratória e modelagem, foi possível avaliar o desempenho de três algoritmos: Multi-Layer Perceptron (MLP), K-Nearest Neighbors (KNN) e Árvore de Decisão.

Durante a análise exploratória, observamos que, apesar da complexidade do processo criativo por trás dos pokémons, era possível identificar alguns padrões relacionados às cores e inspirações nos seres vivos da realidade. Essas informações foram utilizadas no pré-processamento dos dados, juntamente com técnicas como label encoding e one-hot encoding.

Ao avaliar o desempenho dos algoritmos, observamos que o KNN obteve uma acurácia de 53,01% no conjunto de teste, seguido pelo Decision Tree com 44,58% e o MLP com 41,94%. Com base nesses resultados, o modelo selecionado para colocação em produção foi o KNN, devido à sua melhor capacidade de prever o tipo do pokémon.

Em suma, o projeto demonstrou a aplicação prática de algoritmos de classificação em um problema específico, fornecendo insights valiosos sobre o desafio de identificar o tipo de um pokémon com base em suas características básicas. O trabalho futuro poderá se concentrar em melhorar a qualidade dos dados e explorar outras técnicas de modelagem para aprimorar os resultados obtidos.

### Referências

- [The Complete Pokemon Dataset](https://www.kaggle.com/datasets/rounakbanik/pokemon)
- [Pokémon Palette](https://pokemonpalette.com/)
- [Pokémon designed after animals or plants](https://bulbapedia.bulbagarden.net/wiki/User:Reshi643/Pok%C3%A9mon_designed_after_animals_or_plants)
- Pokemanos.ipynb
