import urllib.request, urllib.error, urllib.parse
import re
#from bs4 import BeautifulSoup
import gzip
#https://stackoverflow.com/questions/32202250/python3-urlopen-read-weirdness-gzip?rq=1


#inurl='https://www.sadlerswells.com/' 
inurl = input('input url: ')
#gurl='https://www.google.com/'
#udf = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}
udf = {"User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"}
url = urllib.request.Request(inurl, headers=udf)
urlrsp = urllib.request.urlopen(url)
#print(urlrsp.status, urlrsp.reason)
charset=urlrsp.info().get_content_charset()
#print(charset)
html = gzip.decompress(urlrsp.read()).decode(charset)

#========================
#the following is an example of detecting encoding method in any file
#========================
'''
#check for which encoding it is using for file
import encodings
import pkgutil
import os

def all_encodings():
    modnames = set(
        [modname for importer, modname, ispkg in pkgutil.walk_packages(
            path=[os.path.dirname(encodings.__file__)], prefix='')])
    aliases = set(encodings.aliases.aliases.values())
    return modnames.union(aliases)

encodings = all_encodings()
for enc in encodings:
    try:
        with open(filename, encoding=enc) as f:
            # print the encoding and the first 500 characters
            print(enc, f.read(50))
    except Exception:
        pass'''
#=================================
#Example ends here
#alternative is using chardet to detect #import chardet
#=================================



addr = re.findall('bilibili.com/video/av([0-9]+)',html)
print(addr)
print('https://www.bilibili.com/av'+addr[0])

'''
#soup doc zh https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/#id28
#part 3 of searching the tree
soup = BeautifulSoup(html, 'html.parser')
#tags = soup.find_all('a')
tags=soup.select('a[href]')
#find_all( name , attrs , recursive , string , **kwargs )
#print(soup.prettify())
for tag in tags:
    #soup.find_all(True):
    print({tag.string : tag.attrs})
with open('test.txt', 'wt') as f:
    print(soup.prettify().encode('utf-8'), file=f)'''