from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

driver= webdriver.Chrome(executable_path="C:\Program Files (x86)\driver\chromedriver.exe")
driver.implicitly_wait(10)

driver.get("http://www.itgeared.com/")
driver.maximize_window()

driver.find_element_by_xpath("//*[@id='txtSearch']").click()

wait=WebDriverWait(driver,10)
element= wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='txtSearch']")))
element.click()
time.sleep(5)
driver.close()