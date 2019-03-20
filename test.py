
import os
from bs4 import BeautifulSoup
import requests
import traceback
import urllib
count=0;

def download(url,filename):
    if os.path.exists(filename):
        print('file exisits!')
        return
    try:
        from urllib.request import urlretrieve
        opener=urllib.request.build_opener()
        opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)
        urlretrieve(url,filename)
    except Exception:
        traceback.print_exc()
        if os.path.exists(filename):
            os.remove(filename)



def urlload(url,cnt):
    html=  requests.get(url).text
    soup=BeautifulSoup(html,'html.parser')
    for img in soup.find_all('img'):
        target_url=img['src']
        s=target_url.split('/')
        filename='imgs/'+"".join(s)[6:]
        download(target_url,filename)
        count=cnt+1
        print(count)



if os.path.exists('imgs') is False:
    os.makedirs('imgs')


for i in range(2,100):
    url='http://b34r.com/articlelist/?23-%d.html' % i
    html=  requests.get(url).text
    soup=BeautifulSoup(html,'html.parser')
    for img in soup.find_all('a',target='_blank'):
       imgsrc=img['href']
       imgsrc='http://b34r.com/'+imgsrc
       urlload(imgsrc,count)
       count+=10


