from selenium import webdriver
import time
import csv

driver = webdriver.Chrome(executable_path="C:\\Users\\Bae Soyeon\\Desktop\\python crawling\\chromedriver.exe")

papago_url = 'https://papago.naver.com/'
driver.get(papago_url)

time.sleep(3)

driver.find_element_by_class_name('button#btn_switch__x4Tcl').click()

f = open('C:\\Users\\Bae Soyeon\\Desktop\\python crawling\\my_papago.csv', 'r')
rdr = csv.reader(f)
next(rdr)

my_dict = {}

for row in rdr:
    keyword = row[0]
    korean=row[1]
    my_dict[keyword] = korean
f.close()

while True:
    keyword = input('번역할 영단어 입력: ')
    if keyword == '0':
        print('번역 종료')
        break

    if keyword in my_dict.keys():
        print('이미 번역한 영단어입니다! 뜻은', my_dict[keyword], '입니다.')

    else:
        driver.find_element_by_css_selector('textarea#txtSource').send_keys(keyword)
        driver.find_element_by_css_selector('button#btnTranslate').click()
        time.sleep(1)
    
        output = driver.find_element_by_css_selector('div#txtTarget').text

        my_dict[keyword] = output

        driver.find_element_by_css_selector('textarea#txtSource').clear()
        time.sleep(2)

driver.close()
f.close()



