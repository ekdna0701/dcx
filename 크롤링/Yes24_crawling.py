from bs4 import BeautifulSoup
import requests 

def yes24info(book):
    names = book.find('div',{'class': 'goods_name'})
    bookName = names.find('a').text

    auther = book.find('span',{'class': 'goods_auth'})
    bookAuther = auther.find('a').text

    bookPub = book.find('span',{'class': 'goods_pub'}).text
    bookDate = book.find('span',{'class': 'goods_date'}).text
    bookPrice = book.find('em',{'class': 'yes_b'}).text
    return [bookName, bookAuther, bookPub, bookDate, bookPrice]



url = 'https://www.yes24.com/24/Category/Display/001001046001?ParamSortTp=05&PageNumber=1'
webPage = requests.get(url).text
bsObject = BeautifulSoup(webPage, 'html.parser')       #파싱

tag = bsObject.find('ul', {'class': 'clearfix'})
all_books = tag.findAll('div', {'class': 'goods_info'})


for book_tag in all_books :
    print(yes24info(book_tag))
