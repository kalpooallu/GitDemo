from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver= webdriver.Chrome(executable_path="C:\Program Files (x86)\driver\chromedriver.exe")

driver.get("http://newtours.demoaut.com/")

username = driver.find_element_by_name("userName")
print(username.is_displayed())

username.send_keys("mercury")

pswd=driver.find_element_by_name("password")
print(pswd.is_displayed())

pswd.send_keys("mercury")

driver.find_element_by_name("login").click()
round_trip =driver.find_element_by_xpath('/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[2]/td[2]/b/font/input[1]')
print("status of round trip",round_trip.is_selected())

oneway_trip= driver.find_element_by_xpath('/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[2]/td[2]/b/font/input[2]')
print("status of oneway trip",oneway_trip.is_selected())

driver.close()


