from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome(executable_path="C:\Program Files (x86)\driver\chromedriver.exe")
driver.get("http://www.ironspider.ca/forms/checkradio.htm")

ch=driver.find_elements(By.NAME,"color")
print(len(ch))

radiobutton=driver.find_elements(By.NAME,"browser")
print(len(radiobutton))

ch=driver.find_element(By.XPATH,"//*[@id='Content']/div[1]/blockquote[1]/form/input[6]").is_selected()
print(ch)

driver.find_element(By.XPATH,"//*[@id='Content']/div[1]/blockquote[1]/form/input[5]").click()
time.sleep(10)
ch=driver.find_element(By.XPATH,"//*[@id='Content']/div[1]/blockquote[1]/form/input[5]").is_selected()
print(ch)

rd=driver.find_element(By.XPATH,"//*[@id='Content']/div[1]/blockquote[2]/form/input[1]").is_selected()
print(rd)

rd=driver.find_element(By.XPATH,"//*[@id='Content']/div[1]/blockquote[2]/form/input[2]").is_selected()
print(rd)








