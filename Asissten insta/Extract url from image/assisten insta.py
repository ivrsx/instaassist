import re
from instabot import Bot
import os
from getpass import getpass
from PIL import Image, ImageEnhance, ImageFilter
from pytesseract import image_to_string
from pytesseract import image_to_boxes
import ctypes

def ExportURL():
    image = input('inter photo path ==> ')
    image = image + '.jpg'
    im = Image.open(image)
    im=im.filter(ImageFilter.MedianFilter())
    enhance = ImageEnhance.Contrast(im)
    im = enhance.enhance(2)
    im.convert('1')
    im.save('temp.jpg')
    t = image_to_string(Image.open('temp.jpg'))
    url = re.findall  ('(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-?=%.]+',t)
    output = open('output.txt','a')
    output.write('')
    output.write(str(url))
    output.close()
def upload():
    bot= Bot()
    username = input("username ==> ")
    passwd= getpass("Password ==> ")
    photo = input ('photo dir ==> ')
    discription = open('output.txt','r')
    discription.read()
    discription.close()
    bot.login(username=username,password=passwd)
    bot.upload_photo(photo,caption=discription)

ExportURL()
upload()
ctypes.windll.kernel32.SetThreadExecutionState(0x80000002)
input('Done...')
ctypes.windll.kernel32.SetThreadExecutionState(0x80000000)
