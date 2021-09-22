import requests
from bs4 import BeautifulSoup
import json
import os.path
response=requests.get("https://www.imdb.com/india/top-rated-indian-movies/?ref_=nv_mv_250_in")
soup=BeautifulSoup(response.text,"html.parser")
tbody=soup.find("tbody",class_="lister-list").find_all('tr')
file_exists=os.path.exists("/home/bhagyashri/Desktop/web scraping/oneline_info.json")
def dumping(data):
         with open("/home/bhagyashri/Desktop/web scraping/oneline_info.json","w") as jsonfile:
                json.dump(data,jsonfile,indent=2)
bdic=[]
sr_no=1
for movie in tbody:
    info=movie.find("td",class_="titleColumn").get_text(strip=True)#get_text is necesary
    dic={}
    dic["no"]=sr_no
    dic["info"]=info
    bdic.append(dic)
    sr_no+=1
with open("/home/bhagyashri/Desktop/web scraping/imdbtask1.json","w") as saral:
    json.dump(bdic,saral,indent=4)




