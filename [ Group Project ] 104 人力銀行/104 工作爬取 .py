# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 08:56:24 2021

@author: USER
"""
import requests
import bs4
import pandas as pd
import re, time, requests
from selenium.webdriver import Chrome
from bs4 import BeautifulSoup
import csv


# 加入使用者資訊(如使用什麼瀏覽器、作業系統...等資訊)模擬真實瀏覽網頁的情況
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54  Safari/537.36'}

# 查詢的關鍵字
my_params = {'ro':'1', # 限定全職的工作，如果不限定則輸入0
             'keyword':'資料分析', # 想要查詢的關鍵字
             'isnew':'30', # 只要最近一個月有更新的過的職缺
             'mode':'s'} # 清單的瀏覽模式

url = requests.get('https://www.104.com.tw/jobs/search/?' , my_params, headers = headers).url
driver = Chrome("C:/Users/USER/Desktop/產業新尖兵/爬104/chromedriver.exe")
driver.get(url)

# 網頁的設計方式是滑動到下方時，會自動加載新資料，在這裡透過程式送出Java語法幫我們執行「滑到下方」的動作
for i in range(15): 
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(2)

# 透過BeautifulSoup解析資料
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    List = soup.findAll('a',{'class':'js-job-link'})
    print('共有 ' + str(len(List)) + ' 筆資料')
    jobs = soup.find_all('article',class_='js-job-item') 
    

    for job in jobs:
        print(job.find('a',class_="js-job-link").text)                  #職缺內容
        print(job.get('data-cust-name'))                                #公司名稱
        print(job.find('ul', class_='job-list-intro').find('li').text)  #地址
        print(job.find('span',class_='b-tag--default').text)            #薪資
        print(job.find('a').get('href'))                                #網址
        print('='*70)
        
         
    




