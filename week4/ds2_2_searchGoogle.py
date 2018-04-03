
# -*- coding: utf-8 -*-
import requests
import os
import webbrowser

def searchGoogle():
    url = u'http://www.google.com/'
    query={'q':'python'}
    headers = {'User-Agent' : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"}
    try:
	r=requests.get(url,params=query,headers=headers)
    except requests.exceptions.HTTPError as e:
        print e
        sys.exit(1)
    page=r.text
    print "length: ",len(page)

    # write page
    #fileName=os.path.join(os.getcwd(),'mygoogle.html')
    #f=open(fileName,'w')
    #f.write(page)
    #f.close()
    # open page
    #mygoogle='file://'+'localhost'+fileName
    #print "opening ",mygoogle
    #webbrowser.open(mygoogle)

def main():
    searchGoogle()

if __name__=="__main__":
    main()