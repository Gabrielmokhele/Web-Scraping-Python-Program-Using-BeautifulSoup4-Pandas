import requests
from bs4 import BeautifulSoup
import pandas as pd


with open('stats SA.html', "r", encoding="utf-8") as f:
    doc = BeautifulSoup(f, "html.parser")
    table = doc.find("table")
    headers = table.find_all('th')
    titles = []
    for i in headers:
        title = i.get_text(strip=True)
        titles.append(title)
df = pd.DataFrame(columns=titles)


rows = table.find_all('tr')
for i in rows[1:]:
    data = i.find_all('td')
    row = [tr.get_text(strip=True) for tr in data]
    l = len(df)
    df.loc[l] = row
print(df)
df.to_csv("market.csv")

#url = "https://fbref.com/en/squads/b8fd03ef/2021-2022/all_comps/Manchester-City-Stats-All-Competitions"
#result = requests.get(url)
#doc = BeautifulSoup(result.text, "html.parser")
#table = doc.find("table")
#print(doc.prettify())



