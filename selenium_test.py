import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = os.getcwd() + '\\chromedriver.exe'
print(PATH)

url = 'https://rijkswaterstaatstrooit.nl/'
driver = webdriver.Chrome(PATH)
driver.get(url)

element = driver.find_element_by_class_name('statistic')
print(element.text)
driver.close()