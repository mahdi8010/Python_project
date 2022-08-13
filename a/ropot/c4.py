from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import os
import time 
import random as rn



id='nap.io1024'
password='m123456'
hastag="iamcardib"

#tedad=int(input("tedad lotfan ? "))
tedad=10
driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.instagram.com/accounts/login/')
time.sleep(2)

s1=driver.find_element_by_css_selector('#loginForm > div > div:nth-child(1) > div > label > input')
s1.send_keys(id)

s2=driver.find_element_by_css_selector('#loginForm > div > div:nth-child(2) > div > label > input')
s2.send_keys(password)

time.sleep(2)
s3=driver.find_element_by_css_selector('#loginForm > div > div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.CovQj.jKUp7.DhRcB > button').click()

time.sleep(5)

b=driver.get(f'https://www.instagram.com/{hastag}/')

b=driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

time.sleep(2)

post=driver.find_element_by_css_selector('#react-root > section > main > div > div._2z6nI > article > div:nth-child(1) > div > div:nth-child(4) > div:nth-child(3) > a > div.eLAPa > div._9AhH0')
post.click()

like_ha=driver.find_element_by_css_selector('body > div._2dDPU.QPGbb.CkGkG > div._32yJO > div > article > div > div.HP0qD > div > div > div.eo2As > section.EDfFK.ygqzn > div > div > a')


text=like_ha.text
if text =='likes':
    like_ha.click()
else :
     like_ha=driver.find_element_by_css_selector('')
     like_ha.click('body > div._2dDPU.QPGbb.CkGkG > div._32yJO > div > article > div > div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm > div > div > section.EDfFK.ygqzn > div > span')