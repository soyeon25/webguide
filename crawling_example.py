import requests
from bs4 import BeautifulSoup
import re
webpage = requests.get("***페이지 링크***")
source = BeautifulSoup(webpage.content, "html.parser")


# find_all로 크롤링
data = str(source.find_all(attrs={'class':'***클래스이름***'})) 
data_edit = (re.sub('<.+?>', '', data, 0).strip())
print(data_edit)


#select로 크롤링
for i in range(0,10):
    print(source.select('***.클래스이름***')[i].get_text()) #클래스 이름 앞에 . 꼭 찍기
