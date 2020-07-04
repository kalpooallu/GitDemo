from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome(executable_path="C:\Program Files (x86)\driver\chromedriver.exe")
driver.get("https://www.facebook.com/campaign/landing.php?campaign_id=1653993517&extra_1=s%7Cc%7C318461158215%7Ce%7Cfacebook%20sign%20up%7C&placement=&creative=318461158215&keyword=facebook%20sign%20up&partner_id=googlesem&extra_2=campaignid%3D1653993517%26adgroupid%3D63066387563%26matchtype%3De%26network%3Dg%26source%3Dnotmobile%26search_or_content%3Ds%26device%3Dc%26devicemodel%3D%26adposition%3D%26target%3D%26targetid%3Dkwd-5066597374%26loc_physical_ms%3D1007812%26loc_interest_ms%3D%26feeditemid%3D%26param1%3D%26param2%3D&gclid=EAIaIQobChMIupOfzY3e6AIVVByPCh3xAAgQEAAYASAAEgKPwvD_BwE")
radiobutton=driver.find_element_by_id("u_0_6").is_selected()
print(radiobutton)


driver.find_element_by_id("u_0_7").click()

time.sleep(5)
radiobutton=driver.find_element_by_id("u_0_7").is_selected()
print(radiobutton)

driver.close()