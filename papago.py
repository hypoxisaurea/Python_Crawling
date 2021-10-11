from selenium import webdriver
import time

my_dict = {}
driver = webdriver.Chrome('C:\\Users\\Bae Soyeon\\Desktop\\python crawling\\chromedriver.exe')

papago_url = "https://papago.naver.com/"
driver.get(papago_url)
time.sleep(3)

def get_papago_result(my_dict):
    for i in range(5):
        question = input('번역할 영단어 입력: ')

        driver.find_element_by_css_selector('textarea#txtSource').send_keys(question)
        time.sleep(1)

        driver.find_element_by_css_selector('button#btnTranslate').click()
        time.sleep(1)

        output = driver.find_element_by_css_selector('div#txtTarget').text
        my_dict[question] = output

        driver.find_element_by_css_selector('textarea#txtSource').clear()

    return my_dict

get_papago_result(my_dict)
print(my_dict)
