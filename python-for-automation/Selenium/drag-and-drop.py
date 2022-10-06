from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path=r"C:\Users\Gabe\chromedriver\chromedriver.exe") #passes raw string
driver.maximize_window()
driver.get('http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')

source = driver.find_element('xpath', r'//*[@id="box3"]')
dest = driver.find_element('xpath', r'//*[@id="box103"]')

actions = ActionChains(driver)
actions.drag_and_drop(source, dest).perform()