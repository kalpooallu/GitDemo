from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome(executable_path="C:\Program Files (x86)\driver\chromedriver.exe")
driver.get("https://en-gb.facebook.com/")

element=driver.find_element_by_id("month")
drp=Select(element)

drp.select_by_visible_text("Feb")

# element=driver.find_element_by_id("day")
# drp=Select(element)
# drp.select_by_value("14")

# element=driver.find_element_by_id("year")
# drp=Select(element)
# drp.select_by_value("1993")

print(len(drp.options))

all_options=drp.options
for options in all_options:
    print(options.text)