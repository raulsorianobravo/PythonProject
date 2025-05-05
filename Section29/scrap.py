import requests
from bs4 import BeautifulSoup

r= requests.get("https://pythonizing.github.io/data/example.html")
print(type(r))  
# <class 'requests.models.Response'>

c = r.content

soup = BeautifulSoup(c,"html.parser")
#print(soup.prettify())

# <class 'requests.models.Response'>
# <!DOCTYPE html>
# <html>
#  <head>
#   <style>
#    div.cities {
#     background-color:black;
#     color:white;
#     margin:20px;
#     padding:20px;
# }
#   </style>
#  </head>
#  <body>
#   <h1 align="center">
#    Here are three big cities
#   </h1>
#   <div class="cities">
#    <h2>
#     London
#    </h2>
#    <p>
#     London is the capital of England and it's been a British settlement since 2000 years ago.
#    </p>
#   </div>
#   <div class="cities">
#    <h2>
#     Paris
#    </h2>
#    <p>
#     Paris is the capital city of France. It was declared capital since 508.
#    </p>
#   </div>
#   <div class="cities">
#    <h2>
#     Tokyo
#    </h2>
#    <p>
#     Tokyo is the capital of Japan and one of the most populated cities in the world.
#    </p>
#   </div>
#  </body>
# </html>

all = soup.find_all("div",{"class":"cities"})
#print(all)

# [<div class="cities">
# <h2>London</h2>
# <p>London is the capital of England and it's been a British settlement since 2000 years ago. </p>
# </div>, <div class="cities">
# <h2>Paris</h2>
# <p>Paris is the capital city of France. It was declared capital since 508.</p>
# </div>, <div class="cities">
# <h2>Tokyo</h2>
# <p>Tokyo is the capital of Japan and one of the most populated cities in the world.</p>
# </div>]

first = soup.find_all("div",{"class":"cities"})[0]
print(first)
# <div class="cities">
# <h2>London</h2>
# <p>London is the capital of England and it's been a British settlement since 2000 years ago. </p>
# </div>

head = all[0].find_all("h2")
print(head)
# [<h2>London</h2>]

headName = all[0].find_all("h2")[0].text
print(headName)
# London

for ct in all:
    print(ct.find_all("h2"))
    print(ct.find_all("h2")[0].text)
# [<h2>London</h2>]
# London
# [<h2>Paris</h2>]
# Paris
# [<h2>Tokyo</h2>]
# Tokyo
for ct in all:
    print(ct.find_all("p"))
    print(ct.find_all("p")[0].text)
# [<p>London is the capital of England and it's been a British settlement since 2000 years ago. </p>]
# London is the capital of England and it's been a British settlement since 2000 years ago.
# [<p>Paris is the capital city of France. It was declared capital since 508.</p>]
# Paris is the capital city of France. It was declared capital since 508.
# [<p>Tokyo is the capital of Japan and one of the most populated cities in the world.</p>]
# Tokyo is the capital of Japan and one of the most populated cities in the world.