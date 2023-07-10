from selenium import webdriver      #webdriver을 이용해 해당 브라우저를 열기
from selenium.webdriver.chrome.options import Options       #웹드라이버와 크롬 옵션을 가져오고 선언 

#브라우저 바로 닫힘 방지 
opt = Options()
opt.add_experimental_option('detatch', True)

driver = webdriver.Chrome()
driver.get("http://www.naver.com")

print(driver.title)
print(driver.current_url)