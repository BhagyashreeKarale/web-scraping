import requests
from bs4 import BeautifulSoup
import pprint
response=requests.get("https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/")
soup=BeautifulSoup(response.text,"html.parser")
tab=soup.find("table",class_="table")
movies=tab.find_all("tr")
sr_list=[]
title_list=[]
rating_list=[]
reviewscount_list=[]
link_list=[]
year_list=[]
base="https://www.rottentomatoes.com"
def scrape_task1():
    for k in range(1,len(movies)) :
        tag=movies[k].find_all("td")

        sr=(tag[0]).text.strip()
        sr_list.append(sr)

        rating=(tag[1]).text.strip()
        rating_list.append(rating)

        title=(tag[2]).text.strip()
        name=""
        for i in title:
            if i=="(":#can also use isalpha() and isdigit() for detecting if elements of a string is letter or number
                break
            else:
                name+=i
        title_list.append(name)

        r=len(title)-(len(title)-5)
        title=title[::-1]
        s=""
        for i in range(r+1):
            if title[i] == "(" or title[i]==")":
                pass
            else:
                s+=title[i]
        year=s[::-1]
        year_list.append(year)

        link=base+(tag[2]).a["href"].strip()
        link_list.append(link)

        no_of_reviews=(tag[3]).text.strip()
        reviewscount_list.append(no_of_reviews)

    Top_Movies=[]
    info={}
    for i in range (len(sr_list)):
        info["position"]=sr_list[i]
        info["name"]=title_list[i]
        info["year"]=year_list[i]
        info["rating"]=rating_list[i]   
        info["no. of reviews"]=reviewscount_list[i]
        info["url"]=link_list[i]
        Top_Movies.append(info)
    return(Top_Movies)
#position name year rating url
pprint.pprint(scrape_task1())