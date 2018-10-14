import cv2
import urllib.request as urllib
import numpy as np
from selenium import webdriver
import os
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Chrome()
driver.get('https://www.edmunds.com/alfa-romeo/stelvio/2018/suv/')

first_click32 = driver.find_element_by_xpath(
    '/html/body/div[1]/div/main/div[3]/div/div[1]/div/div[1]/div[2]/div/button/img').click()

time.sleep(2)

try:
    get_data = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[1]/p').text
    print(get_data)
    print(type(get_data))
    getdata = get_data.split()
    gkam = int(getdata[3])
    print(gkam)
except:
    print("Unable to find integer")

# -----------------------------------------------------------------download Code--------------------------------------------

tt = 1
if gkam > 100:
    gkam = 50

while tt < gkam:
    try:
        img = driver.find_element_by_xpath(
            '/html/body/div[5]/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div/div[1]/img')
        src = img.get_attribute('src')
        url = src
        tag = os.getcwd() + "/car " + str(tt) + ".jpg"

        if not os.path.exists(tag):
            req = urllib.urlopen(url)

            arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
            img = cv2.imdecode(arr, -1)  # 'Load it as it is'

            # cv2.imshow('lalala', img)
            try:
                location = os.getcwd() + "/" + str(tt) + " car.jpg"
                cv2.imwrite(location, img)
            except:
                print("bound error")

            try:
                button_path = driver.find_element_by_xpath(
                    '/html/body/div[5]/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div/div[1]/div[4]/button').click()
                if cv2.waitKey() & 0xff == 27: quit()
            except:

                print("path not found 1")
                button_path = driver.find_element_by_xpath(
                    "//*[@class='right carousel-control']").click()
        else:
            print("already exist")
            try:
                button_path = driver.find_element_by_xpath(
                    "//*[@class='right carousel-control']").click()

            except:
                print("path not found 2")
                button_path = driver.find_element_by_xpath(
                    '/html/body/div[5]/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div/div[1]/div[4]/button').click()
    except:
        print("error")
        try:
            button_path = driver.find_element_by_xpath("//*[@class='right carousel-control']").click()

        except:
            print("path not found 3")
            button_path = driver.find_element_by_xpath(
                '/html/body/div[5]/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div/div[1]/div[3]/button').click()

    tt = tt + 1
