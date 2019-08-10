from selenium import webdriver
import time

email = "naaznuzii46@gmail.com"
password = "passwordgrip1"
receiver = "hoorbegum25@gmail.com"
sub = "Recruitment"
msg = "Congratulations!!! \n You are selected."

driver = webdriver.Chrome(executable_path="C:\\Users\\smile\\PycharmProjects\\Pycharm_nuz\\drivers\\chromedriver")
driver.maximize_window()
driver.get("http://www.gmail.com/")
time.sleep(3)
driver.find_element_by_name("identifier").send_keys(email)
driver.find_element_by_id("identifierNext").click()
driver.implicitly_wait(5)
driver.find_element_by_name("password").send_keys(password)
driver.find_element_by_id("passwordNext").click()
driver.find_element_by_css_selector('.aic .z0 div').click()
driver.find_element_by_name("to").send_keys(receiver)
driver.implicitly_wait(5)
driver.find_element_by_name("subjectbox").send_keys(sub)
driver.implicitly_wait(5)
driver.find_element_by_css_selector(".Ar.Au div").send_keys(msg)
driver.implicitly_wait(5)
driver.find_element_by_css_selector("tr.btC td:nth-of-type(1) div div:nth-of-type(2)").click()
time.sleep(4)
driver.close()
print("The email is sent successfully!!!!")
