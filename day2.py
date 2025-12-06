import requests,time,random,csv
from bs4 import BeautifulSoup as bs

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

with open('day2.csv','w',newline='',encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['标题','评分','人数'])

    #循环翻页
    for start in range(0,75,25):

        print(f">>>正在爬取 start={start}")

        try:
            url = f'https://movie.douban.com/top250?start={start}'

            r = requests.get(url,headers=headers,timeout=10)
            r.raise_for_status() # 如果状态码不是200，会抛出异常

            soup = bs(r.text,'lxml')

            #解析数据
            for item in soup.select('.grid_view li,li.item'):
                title = item.select_one('span[class="title"]').text
                rating_span = item.select_one('span[class="rating_num"]')   
                next = rating_span.find_next_siblings('span')
                people = next[1].text  # 索引1表示第二个
                rating = rating_span.text

                w.writerow([title,rating,people])

            # 随机休眠2-3秒，模拟人为操作，避免被封IP
            time.sleep(random.uniform(2,3))
    
        except Exception as e:
            print(f'第{start}页失败:{e}')
            continue

print(f"写入完成，共",75,"条")