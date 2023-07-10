from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import csv

result = []

opt = Options()
opt.add_experimental_option('detach', True)

for i in range(1, 10):
    url = 'https://www.coffeebeankorea.com/store/store.asp'

    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(1)
    try:
        driver.execute_script("storePop2('%d');"%i)
        time.sleep(1)
        html=driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        # print(soup)

        store_name_temp = soup.select("div.store_txt > h2")
        store_name = store_name_temp[0].string
        store_address_temp = soup.select("div.store_txt > table > tbody:nth-child(1) > tr:nth-child(3) > td")
        store_address = store_address_temp[0].text
        store_tel_temp = soup.select("div.store_txt > table > tbody:nth-child(1) > tr:nth-child(4) > td")
        store_tel = store_tel_temp[0].string
        result.append([store_name]+[store_address]+[store_tel])
        # print(store_name, store_address, store_tel)
        driver.quit()
    except:
        continue
print(result)

with open('coffeebean.csv', 'w', newline='', encoding='utf-8')as f:
    csvwriter = csv.writer(f)
    for i in result:
        csvwriter.writerow(i)
