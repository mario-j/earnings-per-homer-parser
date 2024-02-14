import requests
from bs4 import BeautifulSoup, Comment
import sys
sys.stdout.reconfigure(encoding='utf-8')

def getURL(playerName):
    begURL = 'https://www.baseball-reference.com/players/'
    names = playerName.split()
    letter = names[1][0].lower()
    midURL = begURL + letter + '/'
    lastAbr = names[1][0:5].lower()
    firstAbr = names[0][0:2].lower()
    URL = midURL + lastAbr + firstAbr + '01.shtml'
    return URL

for page in range(1,2):
    URL = "https://www.fangraphs.com/leaders/major-league?startdate=&enddate=&month=0&season1=1871&season=2023&type=8&sortcol=4&sortdir=default&pagenum=" + str(page)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    table = soup.find('div', class_='leaders-major_leaders-major__table__hcmbm').find('div', class_='table-fixed').find('table')
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    for row in rows:
        playerData = ['', '', '', '']
        cols = row.find_all(['td', 'th'])
        cols = [ele.text.strip() for ele in cols]
        playerData[0] = cols[1] # name
        playerData[2] = cols[5] # home runs

        playerUrl = getURL(cols[1])
        page = requests.get(playerUrl)
        soup = BeautifulSoup(page.content, "html.parser")

        for comment in soup.find_all(text=lambda text: isinstance(text, Comment)):
            if comment.find("<table ") > 0:
                comment_soup = BeautifulSoup(comment, 'html.parser')
                table = comment_soup.find("table", id='br-salaries')

        salary_total = table.find('tfoot').find('td').text
        position = soup.find('div', id='meta').find('p').text
        playerData[3] = salary_total # career earnings
        playerData[1] = position # position


        print(*playerData, sep=',')
