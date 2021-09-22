# import requests
# from bs4 import BeautifulSoup
# response=requests.get("https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off").text
# file_name="/home/bhagyashri/Desktop/web scraping/first_scraping.html"
# organized_data=BeautifulSoup(response,"html.parser")
# formatted_data=organized_data.prettify()
# with open (file_name,"w") as html_file:
#     html_file.write(formatted_data)
# product=organized_data.find_all("div",{"class":"_13oc-S"})
# product_price=organized_data.find_all("div",{"class":"_3tbKJL"})
# product_rating=organized_data.find_all("div",{"class":"_3LWZlK"})
# sr_no=1
# for products in product:
#     print(str(sr_no)+".","Product Name:",products.div.img["alt"])
#     for i in range(1,len((product_price[sr_no-1]).text)):
#         if ((product_price[sr_no-1]).text)[i]=="₹":
#             final_price=((product_price[sr_no-1]).text)[0:i]
#             break
#     print("    Price:",final_price)
#     print("    Rating:",(product_rating[sr_no-1]).text)
#     print()
#     sr_no+=1
#######################################################################################################
import requests
from bs4 import BeautifulSoup
response=requests.get("https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off").text
file_name="/home/bhagyashri/Desktop/web scraping/first_scraping.html"
organized_data=BeautifulSoup(response,"html.parser")
# formatted_data=organized_data.prettify()
# with open (file_name,"w") as html_file:
#     html_file.write(formatted_data)
product=organized_data.find_all("div",{"class":"_13oc-S"})
product_name=organized_data.find_all("div",{"class":"_4rR01T"})
product_price=organized_data.find_all("div",{"class":"_3tbKJL"})
product_rating=organized_data.find_all("div",{"class":"_3LWZlK"})
sr_no=1
for products in product:
    print(str(sr_no)+".","Product Name:",(product_name[sr_no-1]).text)
    for i in range(1,len((product_price[sr_no-1]).text)):
        if ((product_price[sr_no-1]).text)[i]=="₹":
            final_price=((product_price[sr_no-1]).text)[0:i]
            break
    print("    Price:",final_price)
    if type((product_rating[sr_no-1]).text)!=str:
        print("***Rating unavailable***")
    else:
        print("    Rating:",(product_rating[sr_no-1]).text)
    print()
    sr_no+=1


















