#! /user/bin/evn python
# coding:utf-8
from PIL import Image
from pytesseract import pytesseract

__author__ = 'wgq'

import sys
import os
import requests

LoginUrl = "http://stadm.ecej.com:8081/login/login"
vrifycodeUrl = "https://stbusplatform.ecej.com/site/captchaImage"

resCityChoose = requests.get(vrifycodeUrl)


with open('f:/1.png', 'wb') as f:
    for chunk in resCityChoose.iter_content():
        f.write(chunk)
imge = Image.open('f:/1.png')
ww = pytesseract.image_to_string(imge)
print ww
cookie = requests.utils.dict_from_cookiejar(resCityChoose.cookies).get('SESSION')
print cookie



