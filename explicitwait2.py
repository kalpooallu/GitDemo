from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

driver=webdriver.Chrome(executable_path="C:\Program Files (x86)\driver\chromedriver.exe")

driver.get("http://www.itgeared.com/demo/1502-javascript_countdown.html")

wait=WebDriverWait(driver,20)
element= wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"btnEnable")))
print(element.click())
time.sleep(5)


