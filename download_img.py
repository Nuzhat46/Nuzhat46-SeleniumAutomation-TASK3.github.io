from selenium import webdriver
import os
import json
from urllib.request import *


os.environ["PATH"] += os.pathsep + os.getcwd()
download_path = "C:/Users/smile/Desktop/download/"

image_count = 0
searchtext = input("Enter the search key : ")
extensions = {"jpg", "jpeg", "png", "GIF"}
headers = {}
headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
driver = webdriver.Chrome(executable_path="C:\\Users\\smile\\PycharmProjects\\Pycharm_nuz\\drivers\\chromedriver")
driver.get("https://www.google.co.in/search?q="+searchtext+"&source=lnms&tbm=isch")
if not os.path.exists(download_path + searchtext.replace(" ", "_")):
    os.makedirs(download_path + searchtext.replace(" ", "_"))
images = driver.find_elements_by_xpath('//div[contains(@class,"rg_meta")]')
for img in images:
    img_url = json.loads(img.get_attribute('innerHTML'))["ou"]
    img_type = json.loads(img.get_attribute('innerHTML'))["ity"]
    try:
        if img_type not in extensions:
            img_type = "jpg"
        req = Request(img_url, headers=headers)
        raw_img = urlopen(req).read()
        f = open(download_path + searchtext.replace(" ", "_") + "/" + str(image_count) + "." + img_type, "wb")
        f.write(raw_img)
        f.close
    except Exception as e:
        print("Download complete: {}".format(e))
    image_count+=1
    if image_count == 6:
         break
driver.quit()
print("The download was successful")
