from instabot import Bot
from os import *
import os
from getpass import getpass

bot= Bot()

username = input("username ==> ")
passwd= getpass("Password ==> ")
photo = input ('photo dir ==> ')
discription = input("inter Photo Descriptopn ==> ")
bot.login(username=username,password=passwd)

bot.upload_photo(photo,caption=discription)

os.remove(photo + '.REMOVE_ME')
