from selenium import webdriver
import time

keyword = input('뉴스 검색 키워드: ')

driver = webdriver.Chrome('C:\\Users\\Bae Soyeon\\Desktop\\python crawling\\chromedriver.exe')
news_url = 'https://search.hankyung.com/apps.frm/search.news?query=' + keyword + '&mediaid_clust=HKPAPER,HKCOM'
driver.get(news_url)
time.sleep(2)

xpath_list = ['strong', 'a[1]', 'a[2]']
count = 0

for page_xpath in xpath_list:

    driver.find_element_by_xpath(f'//*[@id="content"]/div[1]/div[2]/div[2]/div/span/{page_xpath}').click()
    ten_articles = driver.find_elements_by_css_selector('em.tit')


    for article in ten_articles:
        title = article.text

        article.click()
        time.sleep(2)

        driver.switch_to.window(driver.window_handles[-1])

        try:
            content = driver.find_elements_by_id('articletxt').text
            seperate = content.split('\n')

            count += 1
            print('[', count, '번 뉴스 - ', title, ']')
            
            for sep in seperate:
                if sep != '':
                    print(sep, end=' ')
            print('\n')
        
        except:
            count += 1
            print('[', count, '번 뉴스 - ', title, ']')

        driver.close()

        driver.switch_to.window(driver.window_handles[0])
        time.sleep(3)

driver.close()