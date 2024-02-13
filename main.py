import requests
from bs4 import BeautifulSoup
import sys
sys.stdout.reconfigure(encoding='utf-8')

for page in range(1,148):
    URL = "https://www.fangraphs.com/leaders/major-league?startdate=&enddate=&month=0&season1=1871&season=2023&type=8&sortcol=4&sortdir=default&pagenum=" + str(page)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    table = soup.find('div', class_='leaders-major_leaders-major__table__hcmbm').find('div', class_='table-fixed').find('table')
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    for row in rows:
        playerData = ['', '']
        cols = row.find_all(['td', 'th'])
        cols = [ele.text.strip() for ele in cols]
        playerData[0] = cols[1]
        playerData[1] = cols[5]
        print(*playerData, sep=',')
