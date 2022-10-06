from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\Gabe\chromedriver\chromedriver.exe") #passes raw string
driver.get('https://demo.seleniumeasy.com/basic-first-form-demo.html') #opens browser at page

#finds message field and sends keys
messageField = driver.find_element('xpath', '//*[@id="user-message"]')
messageField.send_keys('Hello World')

#clicks "Show Message"
showMessageButton = driver.find_element('xpath', '//*[@id="get-input"]/button')
showMessageButton.click()

#A field
aField = driver.find_element('xpath', '//*[@id="sum1"]')
aField.send_keys('2')

#B field
bField = driver.find_element('xpath', '//*[@id="sum2"]')
bField.send_keys('3')

#push total button
totalButton = driver.find_element('xpath', '//*[@id="gettotal"]/button')
totalButton.click()