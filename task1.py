import requests
from bs4 import BeautifulSoup
import os.path
import json
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
for k in range(1,len(movies)) :
    tag=movies[k].find_all("td")
    sr=(tag[0]).text.strip()
    sr_list.append(sr)
    rating=(tag[1]).text.strip()
    rating_list.append(rating)
    title=(tag[2]).text.strip()
    name=""
    for i in title:
        if i=="(":
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
mainlist=[]
for i in range(1,101):
    dic={}
    dic["sr.no"]=sr_list[i-1]
    dic["title"]=title_list[i-1]
    dic["year of release"]=year_list[i-1]
    dic["rating"]=rating_list[i-1]   
    dic["no. of reviews"]=reviewscount_list[i-1]
    dic["link"]=link_list[i-1]
    mainlist.append(dic)
def scrape_toplist():
    with open("/home/bhagyashri/Desktop/web scraping/task1.json","r") as jsonfile:
        data=jsonfile.read()
        p=json.loads(data)
        for i in p:
            if(len(i["sr.no"]))==2:
                print(i["sr.no"],"Name:           ",i["title"])
                print("   Year of release:",i["year of release"])
                print("   Rating:         ",i["rating"])
                print("   No. of reviews: ",i["no. of reviews"])
                print("   Link:           ",i["link"])
                print()
            elif (len(i["sr.no"]))==3:
                print(i["sr.no"],"Name:            ",i["title"])
                print("    Year of release: ",i["year of release"])
                print("    Rating:          ",i["rating"])
                print("    No. of reviews:  ",i["no. of reviews"])
                print("    Link:            ",i["link"])
                print()
            elif (len(i["sr.no"]))==4:
                print(i["sr.no"],"Name:              ",i["title"])
                print("     Year of release:   ",i["year of release"])
                print("     Rating:            ",i["rating"])
                print("     No. of reviews:    ",i["no. of reviews"])
                print("     Link:              ",i["link"])
                print()
file_exists=os.path.exists("/home/bhagyashri/Desktop/web scraping/task1.json")
if file_exists==True:
    scrape_toplist()
else:
    with open("/home/bhagyashri/Desktop/web scraping/task1.json","w") as jsonfile:
        json.dump(mainlist,jsonfile,indent=2)
    scrape_toplist()
            


