from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.firefox.options import Options
import pandas as pd
import numpy as np
from pandas import DataFrame as df
from tabulate import tabulate
import time

options = Options() 
options.add_argument("-headless") 
driver = webdriver.Firefox(options=options)
inventory_sheet = pd.read_excel("/home/swiggityyy/Desktop/mtgtest.xlsx", sheet_name="Library")
df = pd.DataFrame(inventory_sheet)

driver.get("https://www.cardkingdom.com/")
waitsearch = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(("css selector", "#header-search-input"))

)

card_name = driver.find_element(By.CSS_SELECTOR, "#header-search-input")

x = 0

while x < 249:
    time.sleep(2)
    waitsearch = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(("css selector", "#header-search-input")))
    card_name = driver.find_element(By.CSS_SELECTOR, "#header-search-input")
    card_name.clear()
    card_name.send_keys(df.iloc[x,1])
    card_name.send_keys(Keys.RETURN)
    time.sleep(2)
    try:
        price = driver.find_element(By.CLASS_NAME, "stylePrice ")
        df.iloc[x,6] = price.text
    except:
        df.iloc[x,6] = '0'
        print("no price")

    x = x + 1

print(tabulate(df, headers='keys', tablefmt='fancy_grid'))

# # Writes to an excel
df.to_excel("/home/swiggityyy/Desktop/mtgtest.xlsx", sheet_name = "Library", index=False)