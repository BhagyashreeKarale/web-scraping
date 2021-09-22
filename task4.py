import requests
from bs4 import BeautifulSoup
import pprint
def final(text):
    return" ".join(text.split())
def task4(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"html.parser")
    title=(soup.find('h1')).text
    container=soup.find("div",class_="panel-body content_body")
    sub_container=container.find("ul",class_="content-meta info")
    all=sub_container.find_all("li",class_="meta-row clearfix")
    details={}
    for i in all:
        details[(i.find("div",class_="meta-label subtle")).text]=final((i.find("div",class_="meta-value")).text)  
    details["Name:"]=title
    return details
pprint.pprint(task4("https://www.rottentomatoes.com/m/avengers_endgame"))

