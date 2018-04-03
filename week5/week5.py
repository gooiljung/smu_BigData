# -*- coding: utf-8 -*-
import lxml.html

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

tree = lxml.html.fromstring(htmlstr)

for e in tree.cssselect('body :nth-child(1)'):
    print e.text

for e in tree.cssselect('body h1'):
    print e.text
