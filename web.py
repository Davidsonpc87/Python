from bs4 import BeautifulSoup
import csv
import requests

html = requests.get("https://www.climatempo.com.br/").content
soup = BeautifulSoup(html, 'html.parser')
print(soup.prettify())
temperatura = soup.find("span",class_="-text -bold -gray-dark-2 -font-55 _margin-l-15")
#valor = soup.find("span", id = "current-weather-temperature")

print(temperatura.string)
#print(valor.text)

try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td', 'th']):
            csvRow.append(cell.get_text())
            writer.writerow(csvRow)
           
finally:
    csvFile.close()

