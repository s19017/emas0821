import requests
from bs4 import BeautifulSoup

r = requests.get("http://グランブルーファンタジー.gamewith.jp/article/show/20722")
soup = BeautifulSoup(r.text, "html.parser")

file = open('guraburu.txt', 'w')

for i in soup.select("tr"):
    file.write(i.getText() + '\n')

file.close()
