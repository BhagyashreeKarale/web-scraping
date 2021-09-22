import requests
from bs4 import BeautifulSoup
import pprint
response=requests.get("https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/")
soup=BeautifulSoup(response.text,"html.parser")
def scrape_task1():
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
    for i in range (len(sr_list)):
        info={}
        info["position"]=sr_list[i]
        info["name"]=title_list[i]
        info["year"]=int(year_list[i])
        info["rating"]=rating_list[i]   
        info["no. of reviews"]=reviewscount_list[i]
        info["url"]=link_list[i-1]
        Top_Movies.append(info)#info.copy( is necessary when your taking empty dic 'info' outside the for loop
    return(Top_Movies)
# pprint.pprint(scrape_task1())
task1=scrape_task1()
def sort_by_year(movies):
    years=[]
    for i in movies:
        if i["year"] not in years:
            years.append(i["year"])
    dic={}
    for j in years:
        dic[j]=[]
        for k in movies:
            if str(k["year"])==str(j):
                dic[j].append(k)
    return dic
# pprint.pprint(sort_by_year(movies))
task2=sort_by_year(task1)


