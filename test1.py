import cv2
import urllib.request as urllib
import numpy as np

req = urllib.urlopen('https://media.ed.edmunds-media.com/acura/rlx/2018/oem/2018_acura_rlx_sedan_sport-hybrid-sh-awd_e_oem_1_815.jpg')

arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
img = cv2.imdecode(arr, -1) # 'Load it as it is'

cv2.imshow('lalala', img)
cv2.imwrite("face.jpg", img)
if cv2.waitKey() & 0xff == 27: quit()