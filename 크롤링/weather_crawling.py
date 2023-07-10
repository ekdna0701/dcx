from bs4 import BeautifulSoup
import requests
import time     #읽어올 때의 시간 불러오기 
import datetime     
import csv
result = []

with open('sokcho_weather.csv', 'w', newline='') as csvf:        #newline = 빈줄 방지 
    csvwriter = csv.writer(csvf)
    csvwriter.writerow(['연월일', '시분초','온도', '습도', '강수량', '풍향'])

print("Weather Crawling>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
url = 'https://news.nate.com/weather?areaCode=11D20401'
while True :        #무한루프 
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')       #파싱

    #####################################################

    temp = soup.select('#contentsWraper > div.weather_main_today_wrap > div.weather_today > div.today_wrap > div > div.right_today > div.temperature > p.celsius')
    hum = soup.select('#contentsWraper > div.weather_main_today_wrap > div.weather_today > div.today_wrap > div > div.right_today > div.hrw_area > p.humidity > em')
    rain = soup.select('#contentsWraper > div.weather_main_today_wrap > div.weather_today > div.today_wrap > div > div.right_today > div.hrw_area > p.rainfall > em')
    wind = soup.select('#contentsWraper > div.weather_main_today_wrap > div.weather_today > div.today_wrap > div > div.right_today > div.hrw_area > p.wind > em')

    now = datetime.datetime.now()
    yymmdd = now.strftime('%Y-%m-%d')
    hhmmdd = now.strftime('%H:%M:%S')

    result=([yymmdd, hhmmdd, temp[0].text, hum[0].text, rain[0].text, wind[0].text])  #CSV파일 만들 때 result.append 쓰면 대괄호에 대괄호가 됨. 
    with open('sokcho_weather.csv', 'a', newline='') as csvf:        #a : add 
        csvwriter = csv.writer(csvf)
        csvwriter.writerow(result)

    time.sleep(10)

    print(result)
