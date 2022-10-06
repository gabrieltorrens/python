#doesn't work since Earth website updated

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path=r"C:\Users\Gabe\chromedriver\chromedriver.exe") #passes raw string
url = 'https://www.google.com/earth'
driver.get(url)

wait = WebDriverWait(driver, 30) #waits 30 seconds
luckyButton = wait.until(EC.element_to_be_clickable((By.XPATH,r'//*[@id="icon"]')))
luckyButton.click()