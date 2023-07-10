from bs4 import BeautifulSoup

webPage = open ('sample02.html', 'r', encoding='utf-8')     #html 파일 열기, 'r' : 안쓰고 읽기만 할거야 
bsObject = BeautifulSoup(webPage, 'html.parser')     #html파일 파싱(html문서에 포함된 텍스트의 구성 성분을 분해)

# print(bsObject)     #파싱된 것을 출력 

# tag_div = bsObject.find('div')  #find : 파싱된 것 중에서 div 태그 찾음 
# print(tag_div)
# print('****')

# tag_p = bsObject.find('p')   
# print(tag_p)
# print('****')

# tag_p_all = bsObject.findAll('p')     #모든 p태그를 찾음
# print(tag_p_all)
# print('****')

# for i in tag_p_all:       #tag_p_all 이 리스트 형식이니까 원소 하나씩 보기 위해 
#     print(i)
#     print('****')

tag_store_all = bsObject.findAll('p', class_='store')     #p태그의 store 
print(tag_store_all)