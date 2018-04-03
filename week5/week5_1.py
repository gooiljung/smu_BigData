# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

htmlstr = u"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>My Home Page</title>
</head>
<body>
<h1>안녕하십니까</h1>
<p>오늘은 프로그래밍 하는 날...</p>
<p>Today we do programming...</p>
</body>
</html>"""

soup = BeautifulSoup(htmlstr,"lxml")
print soup.select('body > h1')
for e in soup.select('body > h1'):
    print e.text

