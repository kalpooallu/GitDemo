from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="C:\Program Files (x86)\driver\chromedriver.exe")
driver.get("https://www.amazon.in/")

cookie=driver.get_cookies()
print(len(cookie))
print(cookie)

cookie={'name':'mycookie','value':'12345'}
driver.add_cookie(cookie)
cookie=driver.get_cookies()
print(len(cookie))
print(cookie)

driver.delete_cookie('mycookie')
time.sleep(3)
driver.delete_all_cookies()

cookie=driver.get_cookies()
print(len(cookie))
print(cookie)



