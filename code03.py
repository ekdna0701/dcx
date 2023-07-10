from bs4 import BeautifulSoup

html = open("sample02.html", encoding='utf-8')
soup = BeautifulSoup(html, 'html.parser')

p_data = soup.select('p')       #태그 파싱

# print(p_data[1].select('span')[0].string)
# print()
# print(p_data[1].text)

# print(p_data)
# for i in p_data:
#     print(i.text)    #.text 붙이면 text만 추출함 근데 space때문에 가독성 안좋음 
#     print("*****")

for i in p_data:
    for j in i:
        print(j.string.split())     #.strip()
    print("*****")

for i in p_data:
    k = i.get_text().split()    #.split() : ()안에 있는 것 기준으로 데이터를 나눈다 
    print(k)
    # for j in k:
    #     print(j)
    # print("*****")  