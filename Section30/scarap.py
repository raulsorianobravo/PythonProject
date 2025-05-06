import requests
from bs4 import BeautifulSoup

r = requests.get("https://pythonizing.github.io/data/real-estate/rock-springs-wy/LCWYROCKSPRINGS/")
c = r.content
#print(c)  

soup = BeautifulSoup(c,"html.parser")
#print(soup.prettify())

all = soup.find_all("div",{"class":"propertyRow"})
#print(all)

len(all)

#First Element
#print(all[0])

price= all[0].find_all("h4",{"class":"propPrice"})
#print(type(price), "\n", price)

price= all[0].find("h4",{"class":"propPrice"}).text
#print(type(price), "\n", price)
print(price.replace("\n","").replace(" ",""))