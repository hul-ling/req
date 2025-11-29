import requests as req
from bs4 import BeautifulSoup as bs
import csv
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

url = "https://movie.douban.com/top250"

r = req.get(url,headers=headers)
r.encoding = 'utf-8'

soup = bs(r.text,'lxml')

with open('day1.csv','w',newline='',encoding='utf-8-sig') as f:
    w = csv.writer(f)
    w.writerow(['标题','评分'])
    items = soup.select('.grid_view li')

    for item in items:
        title = item.select_one('span.title').text
        rating = item.select_one('span.rating_num').text
        w.writerow([title,rating])
print(f"写入完成，共{len(items)}条")