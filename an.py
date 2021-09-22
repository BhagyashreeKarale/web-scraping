import requests
from bs4 import BeautifulSoup
response=requests.get("https://www.imdb.com/india/top-rated-indian-movies/?ref_=nv_mv_250_in")
soup=BeautifulSoup(response.text,"html.parser")
def movie_scrap():
    tbody=soup.find("tbody",class_="lister-list").find_all('tr')
    for movie in tbody:
        info=movie.find("td",class_="titleColumn").get_text(strip=True)
        print(info)
movie_scrap()
