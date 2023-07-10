from bs4 import BeautifulSoup
import requests 

url = 'https://www.yes24.com/24/Category/Display/001001046001?ParamSortTp=05&PageNumber=1'
webPage = requests.get(url).text
soup = BeautifulSoup(webPage, 'html.parser')       #파싱



#weather_table > tbody
tag_tbody = soup.find('tbody').findAll('tr')         
for region in tag_tbody:
    region_tr = region.findAll('td')
print(region_tr)
