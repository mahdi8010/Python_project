from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import os
import time 
import random as rn



id='sma.group.ir'
password='14000503SMA123'
hastag="نشاسته_گندم"

#tedad=int(input("tedad lotfan ? "))
tedad=5
driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.instagram.com/accounts/login/')
time.sleep(5)

s1=driver.find_element_by_css_selector('#loginForm > div > div:nth-child(1) > div > label > input')
s1.send_keys(id)
time.sleep(5)
s2=driver.find_element_by_css_selector('#loginForm > div > div:nth-child(2) > div > label > input')
s2.send_keys(password)

time.sleep(6)
s3=driver.find_element_by_css_selector('#loginForm > div > div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.CovQj.jKUp7.DhRcB > button').click()

time.sleep(5)

b=driver.get(f'https://www.instagram.com/explore/tags/{hastag}/')

time.sleep(4)
i=0
b=driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
time.sleep(4)
while i <= tedad:


      time.sleep(4)

      post=driver.find_element_by_css_selector('#react-root > section > main > article > div:nth-child(3) > div > div:nth-child(9) > div:nth-child(1) > a > div > div._9AhH0')
      post.click()
      
      time.sleep(4)
      follow_text=driver.find_element_by_css_selector('body > div._2dDPU.QPGbb.CkGkG > div._32yJO > div > article > div > div.HP0qD > div > div > div.UE9AK > div > header > div.o-MQd.z8cbW > div.PQo_0.RqtMr > div.bY2yH > button')
      text=follow_text.text
      
      b=driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
      
      if text =='Follow':
            follow =driver.find_element_by_css_selector('body > div._2dDPU.QPGbb.CkGkG > div._32yJO > div > article > div > div.HP0qD > div > div > div.UE9AK > div > header > div.o-MQd.z8cbW > div.PQo_0.RqtMr > div.bY2yH > button')
            follow.click()
            time.sleep(4)
            like=driver.find_element_by_css_selector('body > div._2dDPU.QPGbb.CkGkG > div._32yJO > div > article > div > div.HP0qD > div > div > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button')
            like.click()
            time.sleep(5)
            exit_post=driver.find_element_by_css_selector('body > div._2dDPU.QPGbb.CkGkG > div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.BI4qX.qJPeX.fm1AK.TxciK.yiMZG > button > div > svg')
            exit_post.click()
      else:
          exit_post=driver.find_element_by_css_selector('body > div._2dDPU.QPGbb.CkGkG > div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.BI4qX.qJPeX.fm1AK.TxciK.yiMZG > button > div > svg')
          exit_post.click()   
      driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
      


print('tamam')