import requests
from bs4 import BeautifulSoup
import json
def final(text):
    return" ".join(text.split())
r=requests.get("https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/")
soup=BeautifulSoup(r.text,"html.parser")
container=soup.find("table",class_="table")
all=container.find_all("tr")
for movies in all:
    d=movies.find_all("td")
    # print(d)
    # break
    # for i in final(d[3].text):
    #     if i.isalpha==True:
    #         print(i,end="")

    for i in range(len(d)):
        if i==2:
            l=list(final(d[i].text))
            for charac in l:
                if charac.isdigit()==True:
                    print(charac,end="")
    print()
