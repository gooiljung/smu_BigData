import requests
from bs4 import BeautifulSoup

def croll():

    r = requests.get("http://python.org")
    page = r.text

    soup = BeautifulSoup(page ,"html.parser")

    news = soup.find("div", class_ = "medium-widget blog-widget" )

    li = news.find_all("li")

    for article in li:
       print article.time['datetime'] , article.a.string


def main():
    croll()



if __name__== "__main__":
    main()
