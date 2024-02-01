from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pyperclip
import pandas as pd
import time

class TwitterScript():
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def open_poke_pallete(self):
        self.driver.get("https://pokemonpalette.com/")
        self.driver.implicitly_wait(10)

    def scrap_pokemon_hex(self):
            df = pd.read_csv('names.csv')
            loginbutton = self.driver.find_element(By.ID, "nameInput")
            loginbutton.click()

            



            for c in range(1, 802):
                row = c - 1
                loginbutton.send_keys(Keys.CONTROL + 'a')

                loginbutton.send_keys(Keys.BACK_SPACE)
                loginbutton.send_keys(c)
                time.sleep(1)

                
                rgb1 = self.driver.find_element(By.XPATH, "//textarea[@class='tweet-input']")
                ActionChains(self.driver).click(rgb1).perform()

                rgb1.send_keys(Keys.CONTROL + 'a')
                rgb1.send_keys(Keys.CONTROL + 'c')
                text = pyperclip.paste()
                time.sleep(1)
                
                

                new_text = text.split('\n')
                if len(new_text) > 2:
        
                    color_list = '\n'.join(line.strip() for line in new_text[2:-2]).split()
                    
                    for c in color_list:
                        print(c)
                    
                    
                    
                    df.at[row, 'hex1'] = color_list[0]
                    df.at[row, 'hex2'] = color_list[1]
                    df.at[row, 'hex3'] = color_list[2]
                
            df.to_csv('your_updated_file.csv', index=False)
