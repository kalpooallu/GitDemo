from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

driver= webdriver.Chrome(executable_path="C:\Program Files (x86)\driver\chromedriver.exe")
driver.implicitly_wait(5)

driver.get("https://www.expedia.com/")
driver.maximize_window()


driver.find_element(By.ID,"tab-flight-tab-hp").click()
driver.find_element(By.ID,"flight-origin-hp-flight").send_keys("NYC")
time.sleep(2)
driver.find_element(By.ID,"flight-destination-hp-flight").send_keys("chicago")
driver.find_element(By.ID,"flight-departing-hp-flight").clear()
driver.find_element(By.ID,"flight-departing-hp-flight").send_keys("04/11/2020")
driver.find_element(By.ID,"flight-returning-hp-flight").clear()
driver.find_element(By.ID,"flight-returning-hp-flight").send_keys("04/15/2020")

# driver.find_element(By.XPATH,"//*[@id='traveler-selector-hp-flight']/div/ul/li/button").click()


driver.find_element(By.XPATH,"//*[@id='gcw-flights-form-hp-flight']/div[8]/label/button").click()

wait=WebDriverWait(driver,10)
element= wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='stopFilter_stops-0']")))
element.click()
time.sleep(5)

driver.quit()

