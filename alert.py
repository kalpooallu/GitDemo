from selenium import webdriver
import time



driver=webdriver.Chrome("C:\Program Files (x86)\driver\chromedriver.exe")
driver.get("http://testautomationpractice.blogspot.com/")

driver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click()
# time.sleep(5)


# driver.switch_to.alert.accept()
driver.switch_to.alert.dismiss()

# WebDriverWait(driver, 5).until(EC.alert_is_present).dismiss()