# 09-classwork: Selenium
[selenium-basics.ipynb](https://github.com/ilenapeng/foundations/blob/main/09-classwork/selenium-basics.ipynb)
### Setup:
``` 
import pandas as pd

import time

from bs4 import BeautifulSoup
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from webdriver_manager.chrome import ChromeDriverManager 
```
### Selenium specifics
* Load webpage: ``` driver.get("url") ```
* Examples of finding things:
* ```driver.find_elements(By.CLASS_NAME, "title")``` - find element with class name "title"
* ```driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_txtName')``` - find element with ID name "ctl00_ContentPlaceHolder1_txtName"
* ```driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_txtName').send_keys('Arnold')``` - type 'Arnold' into the element with that named ID
* ```driver.find_element(By.XPATH, 'Paste XPATH here'``` - if there is no class name or ID
* ```.click()``` to click

### Using Selenium outputs in other ways
* To read a formatted HTML table that you find on a page scraped with selenium: ```df = pd.read_html(table.get_attribute('outerHTML'))[0]```
* To load a page found in Selenium into BeautifulSoup: ```doc = BeautifulSoup(driver.page_source)```
