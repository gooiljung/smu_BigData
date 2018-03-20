
import requests

def readPythonOrg():
    try:
        r = requests.get(u'http://python.org/')
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print e
        sys.exit(1)
    page=r.text
    print "length: ",len(page)
    beg=page.find("Latest News")
    end=page.find("</a></li>",beg)
    print page[beg:end]

def main():
    readPythonOrg()

if __name__=="__main__":
    main()