import pandas as pd
from sqlalchemy import create_engine
import requests
from bs4 import BeautifulSoup as bs
import schedule
import time
import re

schedule.every().saturday.at("22:00").do(crawl_chungbuk)

def crawl_chungbuk():
    for index in range(1,4):
        print(index)
        url = f'https://dorm.chungbuk.ac.kr/home/sub.php?menukey=20041&type={index}'
        raw_html = requests.get(url)
        soup = bs(raw_html.content, 'html.parser')

        for i in soup.find_all("td", {"class":"morning"}):
            for br in soup.find_all("br"):
                br.replace_with(" ")
        for i in soup.find_all("td", {"class":"lunch"}):
            for br in soup.find_all("br"):
                br.replace_with(" ")
        for i in soup.find_all("td", {"class":"evening"}):
            for br in soup.find_all("br"):
                br.replace_with(" ")

        df = pd.read_html(str(soup))
        df = df[0]
        df = df.astype("string")
       
        pattern = r'\([^)]*\)' # 정규표현식 ()삭제
        df["아침"] = df["아침"].str.replace(pat=pattern, repl='', regex=True)
        df["점심"] = df["점심"].str.replace(pat=pattern, repl='', regex=True)
        df["저녁"] = df["저녁"].str.replace(pat=pattern, repl='', regex=True)
      
        
        engine = create_engine('mysql+pymysql://mysql:0963@127.0.0.1:3306/shop')
        conn = engine.connect()
        df["요일"] = df["요일"].str.split(' ').str.get(0)
        df.to_sql(name=f'dorm{index}', con=conn, if_exists='replace', index=False)
        
        

crawl_chungbuk()