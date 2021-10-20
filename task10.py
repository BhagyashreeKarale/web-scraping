import requests
from bs4 import BeautifulSoup
import pprint
import json
import random
import time
import os.path
def task_1():
    file_name="/home/bhagyashri/Desktop/web scraping/all_movie_details.json"
    file_exists=os.path.exists(file_name)
    if file_exists==True:
        with open(file_name,"r") as jsonfile:
            data=jsonfile.read()
            pobj=json.loads(data)
        return pobj
    else:
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
            info["year"]=year_list[i]
            info["rating"]=rating_list[i]   
            info["no. of reviews"]=reviewscount_list[i]
            info["url"]=link_list[i]
            Top_Movies.append(info)
        with open(file_name,"w") as jsonfile:
            json.dump(Top_Movies,jsonfile,indent=2)
        with open(file_name,"r") as jsonfile:
            data=jsonfile.read()
            pobj=json.loads(data)
        return pobj
movies=task_1()
def task_6(movies_list):
    url_list=[]
    for i in movies_list:
        url_list.append(i["url"])
    return url_list
url_list=task_6(movies)
def final(text):                                                                    
    return" ".join(text.split())
def task_8(urlist):
    f=[]
    d={}
    for movie_url in urlist:
        random_sleep=random.randint(1,3)
        id=movie_url[33:]
        file_name="/home/bhagyashri/Desktop/web scraping/task_10/"+id+".json"
        file_exists=os.path.exists(file_name)
        if file_exists == True:
            with open (file_name,"r") as jsonfile:
                data=jsonfile.read()
                p=json.loads(data)
                if p["Original Language:"] not in f:
                    f.append(p["Original Language:"]) 
        else:
            time.sleep(random_sleep)
            response=requests.get(movie_url)
            soup=BeautifulSoup(response.text,"html.parser")
            title=(soup.find('h1')).text
            container=soup.find("div",class_="panel-body content_body")
            sub_container=container.find("ul",class_="content-meta info")
            all=sub_container.find_all("li",class_="meta-row clearfix")
            details={}
            for i in all:
                details[(i.find("div",class_="meta-label subtle")).text]=final((i.find("div",class_="meta-value")).text)  
            details["Name:"]=title
            with open(file_name,"w") as jsonfile:
                json.dump(details,jsonfile,indent=2)  
            with open (file_name,"r") as jsonfile:
                data=jsonfile.read()
                p=json.loads(data)
                if p["Original Language:"] not in f:
                    f.append(p["Original Language:"]) 
    for lang in f:
        d[lang]=[]
        count=0
        for movie_url in urlist:
            id=movie_url[33:]
            file_name="/home/bhagyashri/Desktop/web scraping/task_8/"+id+".json"
            file_exists=os.path.exists(file_name)
            if file_exists == True:
                with open (file_name,"r") as jsonfile:
                    data=jsonfile.read()
                    p=json.loads(data)
                    if p["Original Language:"] == lang:
                        count+=1
        d[lang].append(count) 
    return d    
pprint.pprint(task_8(url_list))


