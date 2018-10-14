import cv2
import urllib.request as urllib
import numpy as np
from selenium import webdriver
import os
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Chrome()
driver.get('https://www.edmunds.com/')

# New Cars Click
first_click = driver.find_element_by_xpath('//*[@id="nav_new_future_makes"]')
first_click.click()

# time.sleep(1)

# CarNameList in second click
second_click = driver.find_elements_by_xpath('//*[@data-tracking-id="nav_mmy_select_make"]')

item_list = []

# fetching item text in list(car Brand name list)
i = 0
for item in second_click:
    text1 = item.text
    item_list.append(text1)

# eliminating spaces from list
item_list = [x for x in item_list if x != '']

print(item_list)

item_list_capital = item_list

# Lower case item list
item_list = [x.lower() for x in item_list]

# Eliminating Spaces and adding - between them
k = []
for hh in item_list:
    j = hh.replace(' ', '-')
    k.append(j)
item_list = k
print(item_list)
#################



"""
#To create folders
while item_list:
    os.mkdir(os.getcwd()+"/"+str(item_list[i]), 0o777)
    i = i + 1
"""

# ----------------------------------------theProgramBegins------------------------------------------------


i = 2
while i < len(item_list):
    xpath_send = '//*[@id="nav"]/div/div/div/div[1]/div[2]/div[2]/a[@href="/' + item_list[i] + '/"]'
    second_click_text = driver.find_element_by_xpath(xpath_send)
    print(item_list[i])
    print(xpath_send)
    second_click_text.click()
    time.sleep(3)

    # ------------------------Creation of third list and filtering-------------------------------------------

    third_layer = driver.find_elements_by_xpath('//*[@data-tracking-id="nav_mmy_model_select"]')
    third_list = []

    for item in third_layer:
        text1 = item.text
        third_list.append(text1)
    print(third_list)
    # print(len(third_list))

    # fourth layer compilation start
    h = 0  # 0
    while h < len(third_list):
        try:
            xpath_send2 = '//*[@id="nav"]/div/div/div/div[1]/div[2]/div[2]/a[' + str(h + 1) + ']'
            print(xpath_send2)
            third_click_text = driver.find_element_by_xpath(xpath_send2)
            print(third_list[h])
            third_click_text.click()
            time.sleep(3)
        except:
            print("third list error " + third_list[h])

        # creating directory for years
        fourth_layer = driver.find_elements_by_xpath('//*[@data-tracking-id="nav_mmy_year_select"]')
        fourth_list = []
        print("------" + str(len(fourth_layer)))
        jk = 0
        for item in fourth_layer:
            text32 = item.text

            y = 0
            if int(text32) == 2018:
                fourth_list.append(text32)
                print("text32:" + str(text32))
                print("fourth List item y :" + str(fourth_list[y]))
                y = y + 1

        for item in fourth_list:
            print("value of jk: " + str(jk))
            fourth_layer[jk].click()


            # ------------------------------------------ downloading image-------------------------------------------------------------------------------


            def dwnld_img(a, b, c, sc, tc):

                first_click32 = driver.find_element_by_xpath(
                    '/html/body/div[1]/div/main/div[3]/div/div[1]/div/div[1]/div[2]/div/button/img').click()

                time.sleep(5)
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
                    gkam = 100

                while tt < gkam:
                    try:
                        img = driver.find_element_by_xpath(
                            '/html/body/div[5]/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div/div[1]/img')
                        src = img.get_attribute('src')
                        url = src
                        tag = os.getcwd() + "/" + str(a) + "/" + b + "/" + \
                              c + "/" + str(third_list[h]) + str(tt) + ".jpg"

                        if not os.path.exists(tag):
                            req = urllib.urlopen(url)

                            arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
                            img = cv2.imdecode(arr, -1)  # 'Load it as it is'

                            # cv2.imshow('lalala', img)
                            try:
                                location = os.getcwd() + "/" + str(a) + "/" + b + "/" + \
                                           c + "/"
                                cv2.imwrite(location + str(third_list[h]) + str(tt) + ".jpg", img)
                            except:
                                print("bound error")
                            try:
                                button_path = driver.find_element_by_xpath(
                                    "//*[@class='right carousel-control']").click()

                            except:

                                print("path not found 1")
                                button_path = driver.find_element_by_xpath(
                                    '/html/body/div[5]/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div/div[1]/div[4]/button').click()
                            # if cv2.waitKey() & 0xff == 27: quit()
                        else:
                            print("already exist")
                            try:
                                button_path = driver.find_element_by_xpath(
                                    '/html/body/div[5]/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div/div[1]/div[4]/button').click()
                            except:
                                button_path = driver.find_element_by_xpath(
                                    "//*[@class='right carousel-control']").click()
                                print("path not found 2")
                    except:
                        print("error")
                        try:
                            button_path = driver.find_element_by_xpath(
                                '/html/body/div[5]/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div/div[1]/div[4]/button').click()
                        except:
                            button_path = driver.find_element_by_xpath(
                                "//*[@class='right carousel-control']").click()
                            print("path not found 3")
                    tt = tt + 1
                try:
                    close_button = driver.find_element_by_xpath(
                        '/html/body/div[5]/div/div[1]/div/div/div/button').click()
                except:
                    print("X button path not found 4")
                    driver.refresh()
                time.sleep(1)

                try:
                    first_click_1 = driver.find_element_by_xpath('//*[@id="nav_new_future_makes"]')
                    first_click_1.click()
                    time.sleep(2)

                    second_click45 = driver.find_element_by_xpath(sc)
                    second_click45.click()
                    time.sleep(2)

                    third_click45 = driver.find_element_by_xpath(tc)
                    third_click45.click()
                    time.sleep(3)
                except:

                    first_click_1 = driver.find_element_by_xpath('//*[@id="nav_new_future_makes"]')
                    while first_click.click() is not True:
                        print("not true again....")
                        driver.refresh()
                        time.sleep(5)

                    time.sleep(2)

                    second_click45 = driver.find_element_by_xpath(sc)
                    second_click45.click()
                    time.sleep(2)

                    third_click45 = driver.find_element_by_xpath(tc)
                    third_click45.click()
                    time.sleep(3)


            dwnld_img(item_list_capital[i], third_list[h], fourth_list[0], xpath_send, xpath_send2)

            jk = jk + 1

        print(fourth_list)

        h = h + 1
        back_click = driver.find_element_by_xpath('//*[@id="nav"]/div/div/div/div[1]/div[2]/div[1]/a[2]').click()

    i = i + 1
    back_click = driver.find_element_by_xpath('//*[@id="nav"]/div/div/div/div[1]/div[2]/div[1]/a').click()
