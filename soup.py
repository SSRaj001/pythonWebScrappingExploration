import requests
import pandas as pd
from bs4 import BeautifulSoup

URL = 'http://marscolepcdecry.s3-website.ap-south-1.amazonaws.com/'
page = requests.get(URL)

# Saving the HTML into a file
soup = BeautifulSoup(page.content, 'html5lib')
with open("Output.html", "w", encoding='utf-8') as file:
    file.write(str(soup.prettify()))

# Finding elements by ID
results = soup.find(id='header')
print(results.prettify())

# Finding Elements by HTML Class Name
listElem = soup.find_all('div', class_='row')

for elem in listElem:
    print(elem.prettify())

# Extracting test from HTML elements
extTest = soup.find_all('div', class_='Message')
print(extTest[0].text)

# select
print(soup.select('div span'))

# Creating Dataframe and exporting it as csv
URL2 = "https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/"
page2 = requests.get(URL2)

soup2 = BeautifulSoup(page2.text, 'html5lib')
countryList, confirmedCountList, deathList = [], [], []
data_iterator = iter(soup2.find_all('td'))
while True:
    try:
        country = next(data_iterator).text
        confirmed = next(data_iterator).text
        deaths = next(data_iterator).text
        continent = next(data_iterator).text
        countryList.append(country)
        confirmedCountList.append(int(confirmed.replace(',', '')))
        deathList.append(int(deaths.replace(',', '')))
    except StopIteration:
        break
df = pd.DataFrame({
    "Country": countryList,
    "Confirmed Cases": confirmedCountList,
    "Death Counts": deathList
})
df.to_csv('data.csv')
