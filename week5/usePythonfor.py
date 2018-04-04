import requests
from bs4 import BeautifulSoup

def croll():

    r = requests.get("http://python.org")
    page = r.text

    soup = BeautifulSoup(page ,"html.parser")

    news = soup.find("div", class_ = "applications-widget")

    menu = news.find("ul", class_ = "menu")
    li = menu.find_all("li")
    for x in li:
        print x.b.string + ":"
        for result in x.find_all("a",class_="tag"):
            print result.string


def main():
    croll()



if __name__== "__main__":
    main()
