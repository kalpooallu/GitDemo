from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path="C:\Program Files (x86)\driver\chromedriver.exe")
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()
source=driver.find_element_by_id("box7")
target=driver.find_element_by_id("box107")
actions=ActionChains(driver)
actions.drag_and_drop(source,target).perform()