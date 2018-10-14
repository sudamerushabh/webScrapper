import cv2
import urllib.request as urllib
import numpy as np
from selenium import webdriver
import os
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Chrome()
driver.get('https://www.edmunds.com/acura/ilx/2018/sedan/')

image_click = driver.find_element_by_xpath('/html/body/div[1]/div/main/div[3]/div/div[1]/div/div[1]/div[1]/div/button/img').click()

time.sleep(1)
close_button = driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/div/div/div/button/i').click()

menu_click = driver.find_element_by_xpath('//*[@id="nav_new_future_makes"]').click()






