import requests
from bs4 import BeautifulSoup

keyword = input("뉴스 검색 키워드: ")
count = 0

for page in range(1, 3):
    news_url = 'https://search.hankyung.com/apps.frm/search.news?query=' + keyword + '&mediaid_clust=HKPAPER, HKCOM&page=' +  str(page)
    
    raw = requests.get(news_url)

    soup = BeautifulSoup(raw.text, 'html.parser')

    box = soup.find('ul', {'class' : 'article'})
    all_title = box.find_all('em', {'class' : 'tit'})
    all_date = box.find_all('span', {'class' : 'date_time'})

    
    for title in all_title:
        for date in all_date:
            x = date.text
        count += 1
        t = title.text
        print(count, '- [', x, ']', t.strip())


        