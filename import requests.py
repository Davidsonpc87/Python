
#from bs4 import BeautifulSoup
#url = 'https://www.example.com'
#response = requests.get(url)
#soup = BeautifulSoup(response.text, 'html.parser')
#title = soup.title.string
#print(title)
#import requests
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://en.wikipedia.org/wiki/Comparison_of_text_editors')
bs = BeautifulSoup(html, 'html.parser')
table = bs.findAll('table', {'class': 'wikitable'})[0]
rows = table.findAll('tr')
csvFile = open('Arquivo_Teste.csv', 'wt+')
writer = csv.writer(csvFile)
try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td', 'th']):
            csvRow.append(cell.get_text())
            writer.writerow(csvRow)
           
finally:
    csvFile.close()