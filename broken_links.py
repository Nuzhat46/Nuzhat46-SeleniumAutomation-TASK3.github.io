from selenium import webdriver
import requests
import time

driver = webdriver.Chrome(executable_path="C:\\Users\\smile\\PycharmProjects\\Pycharm_nuz\\drivers\\chromedriver")
driver.maximize_window()
driver.get("http://www.google.co.in/")
links = driver.find_elements_by_css_selector("a")
print("Total number of links: ", len(links))

for link in links:
    req = requests.head(link.get_attribute('href'))
    if req.status_code >= 400:
        print(link.get_attribute('href'), req.status_code)
    else:
        print(link.get_attribute('href') + "--link is OK")
time.sleep(5)
driver.quit()
print("The Test is completed")