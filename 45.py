import pyautogui as p
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
username ="shivanshagarwal872"
password ="84572005"
driver = webdriver.Chrome()
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(3)
driver.find_element(By.NAME , "username").send_keys(username)
driver.find_element(By.NAME , "password").send_keys(password)
driver.find_element(By.XPATH, '//*[@type="submit"]').click()
time.sleep(50) 