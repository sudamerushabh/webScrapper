import os
import cv2
import urllib.request as urllib
import numpy as np
from selenium import webdriver
import os
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

try:
    if 0<1:
        print("rushabh")

except:
    print("fuck off")

l = ['ACURA', 'ALFA ROMEO', 'ASTON MARTIN', 'AUDI', 'BENTLEY', 'BMW', 'BUICK', 'CADILLAC', 'CHEVROLET', 'CHRYSLER', 'DODGE', 'FERRARI', 'FIAT', 'FORD', 'GENESIS', 'GMC', 'HONDA', 'HYUNDAI', 'INFINITI', 'JAGUAR', 'JEEP', 'KIA', 'LAMBORGHINI', 'LAND ROVER', 'LEXUS', 'LINCOLN', 'LOTUS', 'MASERATI', 'MAZDA', 'MCLAREN', 'MERCEDES-BENZ', 'MINI', 'MITSUBISHI', 'NISSAN', 'PORSCHE', 'RAM', 'ROLLS-ROYCE', 'SMART', 'SUBARU', 'TESLA', 'TOYOTA', 'VOLKSWAGEN', 'VOLVO']

l = [x for x in l if x != '']

print(l)

l = [x.lower() for x in l]
print(l)


#xpath = "//label[contains(text(),'%s')]/.." % newrooomtime

#//span[contains(text(),'Users')

k = []
for i in l:
    j = i.replace(' ','-')
    k.append(j)
#l = [x.strip(' ') for x in l]
print(k)
print(os.getcwd())
i=0
while l:
    os.mkdir(os.getcwd()+"/"+str(l[i]), 0o777)
    i = i + 1

    # this code is to create directory
    # k = 0
    # while k < len(third_list):
    #    try:
    #       dir = os.getcwd() + "/" + str(item_list_capital[i]) + "/" + third_list[k]
    #      if not os.path.exists(dir):
    #         os.mkdir(dir, 0o777)
    # except(FileNotFoundError, IOError):
    #   print("file not found")
    # k = k + 1

    req = urllib.urlopen(url)

    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    img = cv2.imdecode(arr, -1)  # 'Load it as it is'

    cv2.imshow('lalala', img)
    cv2.imwrite("face.jpg", img)
    if cv2.waitKey() & 0xff == 27: quit()
