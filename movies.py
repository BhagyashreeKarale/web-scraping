import requests
from bs4 import BeautifulSoup
response=requests.get("https://www.imdb.com/india/top-rated-indian-movies/?ref_=nv_mv_250_in")
soup=BeautifulSoup(response.text,"html.parser")
title1=soup.title
#task1:all 250 movies details
def scrape_top_list():
    main_div=soup.find("div",{"class":"lister"})
    tbody=main_div.find("tbody",{"class":"lister-list"})
    trs=tbody.find_all("tr")
    sr_no=1
    for tr in trs:
        title=(tr.find("td",{"class":"titleColumn"}).a).text#another way:class_="titleColumn"
        print(str(sr_no)+"."+title)
        year=(tr.find("td",{"class":"titleColumn"}).span).text
        print("  Year of release:",year.strip("()"))#anotherway:.replace("(","").replace(")","")
        rating=tr.find("td",{"class":"ratingColumn imdbRating"}).strong.text#another way:rating=tr.find("td",{"class":"ratingColumn imdbRating"}).strong.get_text()
        print("  Rating:",rating)
        url = (tr.find("td",{"class":"titleColumn"})).a['href']
        movie_url="https://www.imbd.com"+url
        print("  Movie link:",movie_url)
        print()
        sr_no+=1
#movies list according to year  
scrape_top_list()
