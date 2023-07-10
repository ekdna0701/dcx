from bs4 import BeautifulSoup

webPage = open ('sample02.html', 'r', encoding='utf-8')
bsObject = BeautifulSoup(webPage, 'html.parser') 


apple=bsObject.select('#fruits2')       #객체생성
print(apple[0].select('span'))      #0번째거에서 select하겠다 
