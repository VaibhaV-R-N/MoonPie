import requests as req
from bs4  import BeautifulSoup as bs
import json

page = req.get('https://daily.pokecommunity.com/2017/11/17/pokemon-ultra-sun-and-ultra-moon-alola-dex-locations-and-more/')

soup = bs(page.content, 'html.parser')
trs = soup.findAll('tr')
lis = []

for tr in trs:
    tds = tr.findAll('td')
    lis1 = []
    if len(tds)>0:
        for td in tds:
            lis1.append(td.text)
        lis.append(lis1)
 

for i in range(2):
    for l in lis:
        try:
            if l[5]=='':
                lis.remove(l)

            l[1] = l[1].strip("\n")
            l[2] = l[2].replace("\n",",")
            l[3] = l[3].replace("\n",",")

        except:
            pass
locations = {}

for l in lis:
    locations[str(l[1]).lower()] = l[5].split(',')

jo = json.dumps(locations, indent=4)

with open('Spawn.json','w') as file:
    file.write(jo)


