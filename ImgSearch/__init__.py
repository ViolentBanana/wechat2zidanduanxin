import re



str= '<p>< img src="aa" alt="">< img src="bb" alt="" srcset=""></p >'

imgs = re.findall('< img src="(.*?)" alt=', str, re.S)
for url in imgs:
    print url
