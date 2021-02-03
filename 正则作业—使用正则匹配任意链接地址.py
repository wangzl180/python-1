import re
import urllib.request



string = 'https://blog.csdn.net/u011225629 '
response = urllib.request.urlopen(string)
html = response.read()
print(html)
pattern = re.compile(r'\w+://(?:[\w $-_@.&+])+')

url = re.findall(pattern, str(html))
print(url)
with open(r'C:\Users\edz\Desktop\aa.txt','r+',encoding='utf-8') as f:
    for i in url:
        f.write(i+'\n')
        print(i,'\n')












# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%s*%s=%s"%(i,j,i*j),end=" ")
#     print( )