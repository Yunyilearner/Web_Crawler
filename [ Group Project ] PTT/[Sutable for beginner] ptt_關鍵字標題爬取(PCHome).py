# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 2021

@author: yunyi
"""

# In[] PCHome 爬取

import requests
from bs4 import BeautifulSoup
import pandas as pd  #導入 pandas 模組，可以把寫程式產生的 dataframe 存成 excel csv 等檔案


# 利用迴圈抓取多頁八卦版網頁資訊
for i in range(15):
    URL = "https://www.ptt.cc/bbs/Gossiping/search?page="+str(i)+"&q=PCHome"
    print(URL)
    
    my_header = {"cookie": "over18= 1"}  #cookie 會塞在 headers 裡
    
    #發送請求
    ppt_response = requests.get(URL, headers= my_header)
    print(ppt_response.status_code)
    
    ppt_sp = BeautifulSoup(ppt_response.text,"html.parser")
    
    #抓取目標內容所在標籤: <div class='title'> 
    titles = ppt_sp.find_all('div', 'title')
    print(titles)
    
   #萃取標籤中，title 的文字出來
   #for t in titles:        
   #    print(t.text)      
    for t in titles:
        print(t.text.strip())  #strip 不空行  
        
    # 將萃取出來的文字存入我們創建的 list 中
    title_list = []      
    for t in titles:
        title_list.append(t.text.strip())
    print(title_list)
        
    # 將 list 改成能存取成 csv 的 dataframe 格式    
    PCHomeDataframe = pd.DataFrame()  #注意指令寫法 DataFrame
    
     # 中括號命名 DataFrame 欄位名稱
    PCHomeDataframe['title'] = title_list
    print(PCHomeDataframe)
    
    # 存多個檔案，需要改變要存檔的檔案名稱，才不會出現重複檔名
    #path = 'C:/Users/yuniy/Desktop/New pioneers in the industry/Python-Programming Language/Web_Crawler/Beautiful_Soup'
    
    PCHomeDataframe.to_csv('PCHome'+str(i)+'.csv', index = False, encoding = "utf-8-sig")

      
            
#讀取目標檔案的位置
from glob import glob 
import pandas as pd 
# 將資料夾內所有 csv 檔案存到 files 中
files = glob('*.csv')
print(files)
  
#合併檔案
combine_PCHomeDF = pd.concat(
    (pd.read_csv(file, usecols=['title'], encoding='utf-8-sig') for file in files), ignore_index=True)

print(combine_PCHomeDF)

#儲存檔案
combine_PCHomeDF.to_csv('PCHome.csv', index = False, encoding = "utf-8-sig")
    
    
#讀取合併的 csv 檔   
df = pd.read_csv('PCHome.csv')
#print(df)

#尋找與送貨速度相關的關鍵字
keyword_24hr = df.loc[df['title'].str.contains("24" or "送貨" or "速度")]
print(keyword_24hr)


#存取檔案
keyword_24hr.to_csv('PCHomekeyword.csv', index=False,encoding='utf-8-sig')


# In[] 






































