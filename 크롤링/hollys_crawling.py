from bs4 import BeautifulSoup
import requests
result = []


print("Hollys store Crawling>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
re = input("검색할 지역은? : ")
for page in range(1, 11):
    url='https://www.hollys.co.kr/store/korea/korStore2.do?pageNo=%d&sido=%s&gugun=&store='%(page, re)     #페이지여러개 분석하기 위해 페이지부분 %d로 바꿔줌
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')       #파싱

    # tag_tbody_s = soup.select('#contents > div.content > fieldset > fieldset > div.tableType01 > table > tbody')    #select는 list로 저장됨
    tag_tbody_f = soup.find('tbody').find_all('tr')      #find는 문자열, findall은 리스트로 저장됨 
    for store in tag_tbody_f:
        store_td = store.findAll('td')
        store_name = store_td[1].string     #매장명
        store_sido = store_td[0].string     #시/도
        store_address = store_td[3].string     #주소
        store_phone = store_td[5].string     #전화
        result.append([store_name, store_sido, store_address, store_phone])

    with open("HollysList.text", 'w', encoding='utf-8') as f :      #csv파일로 넘기려면 txt파일로 먼저 만들어준다. 
        f.write('매장명\t지역\t주소\t전화번호\n')
        for i in result:
            for j in i:
                f.write(str(j)+'\t')        #write함수는 반드시 문자열로 들어가야하기 때문에str 사용, tab로 구분하기 위해 \t 
            f.write('\n')       #줄바꿈

