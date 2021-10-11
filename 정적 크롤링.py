from bs4 import BeautifulSoup #BeautifulSoap 라이브러리 import
import requests #requests 라이브러리 import

lotto_url = 'https://dhlottery.co.kr/gameResult.do?method=byWin' #lotto 사이트 주소를 변수에 저장
raw = requests.get(lotto_url) #get 메소드를 이용해 페이지의 내용 요청

soup = BeautifulSoup(raw.text, 'html.parser') #raw.text를 실제 HTML 코드로 변환

box = soup.find('div', {'class' : 'nums'}) #HTML 코드에서 <div class="nums"> 태그를 찾아 변수에 저장
numbers = box.find_all('span') #nums 안의 모든 span 태그 추출, 변수에 저장

print('< 최근 로또 당첨 번호 >')
for number in numbers: #한 줄씩 출력되도록 반복문 지정
    print(number.text) #태그의 텍스트 데이터만 출력
