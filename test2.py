import cv2
import urllib.request as urllib
import numpy as np
from selenium import webdriver
import os
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def funcs1():
    driver = webdriver.Chrome()

    driver.get('https://www.edmunds.com/acura/ilx/2018/sedan/')

    first_click = driver.find_element_by_xpath(
        '/html/body/div[1]/div/main/div[3]/div/div[1]/div/div[1]/div[1]/div/button/img').click()

    time.sleep(3)
    get_data = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[1]/p').text
    print(get_data)
    print(type(get_data))
    getdata = get_data.split()

    gkam = int(getdata[3])
    print(gkam)
    tt = 1
    while tt < gkam:
        try:
            img = driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div/div[1]/img')
            src = img.get_attribute('src')
            url = src

            req = urllib.urlopen(url)

            arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
            img = cv2.imdecode(arr, -1)  # 'Load it as it is'

            # cv2.imshow('lalala', img)

            cv2.imwrite("car "+str(tt)+".jpg", img)
            button_path = driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div/div[1]/div[4]/button').click()
            if cv2.waitKey() & 0xff == 27: quit()
        except:
            print("error")
            button_path = driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div/div[1]/div[4]/button').click()
        tt = tt + 1



funcs1()
