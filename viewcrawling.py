from bs4 import BeautifulSoup
from selenium import webdriver      #webdriver을 이용해 해당 브라우저를 열기
from selenium.webdriver.chrome.options import Options   
import time   
# import requests   
import csv
result = []

url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query="  #query 뒤에는 사용자로부터 입력받아서 사용할 것 
keyword = input("검색어를 입력해주세요 : ")

search_url = url+ keyword
# html = requests.get(search_url).text

#브라우저 바로 닫힘 방지 
opt = Options()
opt.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opt)
driver.get(search_url)
time.sleep(2)

for i in range(3):
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(2)

html = driver.page_source


soup = BeautifulSoup(html, 'html.parser')
print(soup)


############################
items = soup.select(".api_txt_lines.total_tit")  #가져오고 싶은 것의 공통된 class 복붙, class면 앞에 . 찍어주고 id는 #

for i, item in enumerate (items, 1) :      #enumerate : 인덱스와 값을 같이 가져옴 / index번호 1번부터 가져오기 
    print(f"{i}:{item.text}, {item.attrs['href']}") #href(속성)의 속성값을 가져온다 
    result.append([i, item.txt, item.attrs['href']])

driver.quit()       #창 닫기

# with open(f'{keyword}.csv', 'w', newline='', encoding='utf-8')as f:
#     csvwriter = csv.writer(f)
#     for i in result:
#         csvwriter.writerow(i)