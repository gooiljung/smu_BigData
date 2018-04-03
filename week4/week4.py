from urllib import urlopen
keyword = 'python'
resp = urlopen('https://www.google.com/search?q='+keyword)
html = resp.read()
print len(html)
print html[100:200]
