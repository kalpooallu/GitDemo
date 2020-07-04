from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\Program Files (x86)\driver\chromedriver.exe")

driver.get("https://www.selenium.dev/")
print(driver.title)
print(driver.current_url) 
# print(driver.page_source)
driver.close()
