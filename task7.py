import requests
from bs4 import BeautifulSoup
import pprint
import os.path
import json
def final(text):
    return" ".join(text.split())
def task_7(movie_url):#https://www.rottentomatoes.com/m/black_panther_2018
    id=movie_url[33:]
    file_name="/home/bhagyashri/Desktop/web scraping/"+id+".json"
    file_exists=os.path.exists(file_name)
    if file_exists == True:
        with open (file_name,"r") as jsonfile:
            data=jsonfile.read()
            p=json.loads(data)
            return p
    else:
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
            return p      
pprint.pprint(task_7("https://www.rottentomatoes.com/m/logan_2017"))


