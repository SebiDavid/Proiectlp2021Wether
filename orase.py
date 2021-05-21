import requests
from bs4 import BeautifulSoup
import pandas




url = 'https://ro.metapedia.org/wiki/Lista_ora%C5%9Felor_din_Rom%C3%A2nia'
my_headers = {"User-Agent": "Mozilla/5.0"}
page = requests.post(url,headers=my_headers)
soup = BeautifulSoup(page.content, 'html.parser')

tbody = soup.find("tbody")

orase = []
for i in tbody.find_all('a'):
    orase.append(i.text)


print(orase)

df = pandas.DataFrame({'Orase':orase})
print(df)

df.to_csv('orase.csv',encoding='utf-8-sig')


