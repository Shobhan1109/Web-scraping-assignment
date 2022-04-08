from bs4 import BeautifulSoup
import requests
import pandas

link = "https://www.flipkart.com/search?q=iphone%2013&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

page = requests.get(link)
soup = BeautifulSoup(page.content, "html.parser")

name = []
price = []
star = []
features = []

for i in soup.findAll("div", class_="_3pLy-c row"):
    product_name = i.find("div", attrs={"class" : "_4rR01T"})
    product_price = i.find("div", attrs={"class" : "_30jeq3 _1_WHN1"})
    product_star = i.find("div", attrs={"class":"_3LWZlK"})
    product_features = i.find("ul", attrs={"class":"_1xgFaf"})
    name.append(product_name.text)
    price.append(product_price.text)
    star.append(product_star.text)
    features.append(product_features.text)

data = pandas.DataFrame({"Product name":name,"Product price":price,"Product features":features,"Product star":star})
print(data.head())
data.to_csv("Flipkart.csv")