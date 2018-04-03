import urllib2
import os
url = 'http://www.google.com/#q=python'

headers = {
    'User-agent' : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",

}

request = urllib2.Request(url, None, headers)
response = urllib2.urlopen(request)
print response.headers

html = response.read()
print len(html)

f = open(os.path.join('./', 'mygoogle.html'), 'w') # os.path.join 운영체제마다 디렉토리가 달라서 사용
f.write(html)
f.close()

