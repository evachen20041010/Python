import requests
from bs4 import BeautifulSoup
 
payload = {
    "from":"/bbs/Gossiping/index.html",
    "yes":"yes"
}
session = requests.session()
 
session.post("https://www.ptt.cc/ask/over18", data= payload)
res = session.get("https://www.ptt.cc/bbs/Gossiping/index.html")
#print(res.text)
soup=BeautifulSoup(res.text, features="lxml")
#選取.r-ent的所有元素，接著一筆一筆處理
for rent in soup.select('.r-ent'):
    #再進一步選取.title元素，並取得第一筆資料
    element = rent.select('.title')[0]
    title = element.text.strip()
    element = rent.select('.author')[0]
    author = element.text
    element= rent.select('.date')[0]
    date = element.text
    print(f'標題:{title}, 作者: {author}, 日期: {date}')
    #印出分隔線
    print('-'*50)