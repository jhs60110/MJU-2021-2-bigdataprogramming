import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
import os

start = 1
result_df = pd.DataFrame()

while True:
    try:

        url = 'https://search.naver.com/search.naver?&where=news&query=%EB%B0%98%EB%A0%A4%EA%B2%AC&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=3&ds=2020.01.01&de=2021.01.09&docid=&nso=so:r,p:from20200101to20210109,a:all&mynews=0&cluster_rank=91&start={}&refresh_start=0'.format(
            start)
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
                   'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
       # news_title = [title['title'] for title in soup.find_all('a', attrs={'class':'news_tit'})] # 기사 제목

       # dates = [ date.get_text() for date in soup.find_all('span', attrs={'class':'info'})] # 기사 작성일
        texts = [text.get_text() for text in soup.find_all(
            'a', attrs={'class': 'api_txt_lines dsc_txt_wrap'})]

        news_date = []
       # for date in dates:
        #    if re.search(r'\d+.\d+.\d+.', date) != None: # 기사 작성일 정제
        #       news_date.append(date)

        df = pd.DataFrame({'내용': texts})
        result_df = pd.concat([result_df, df], ignore_index=True)
        start += 10

    except:  # 오류발생시 몇 페이지까지 크롤링했는지 page를 확인하기
        print(start)
        break

folder_path = os.getcwd()
#xlsx_file_name = 'naver_news.xlsx'
#result_df.to_excel(xlsx_file_name)
result_df.to_csv('newslist.txt')
#print('엑셀 저장 완료 | 경로 : {}\\{}'.format(folder_path))
os.startfile(folder_path)
