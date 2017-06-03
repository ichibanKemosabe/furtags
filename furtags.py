#!/usr/bin/env python

import requests
import urllib2
from bs4 import BeautifulSoup

imageToSearch = 'fur.jpg'

searchUrl = 'http://www.google.com/searchbyimage/upload'
multipart = {'encoded_image': (imageToSearch, open(imageToSearch)), 'image_content': ''}
response = requests.post(searchUrl, files=multipart, allow_redirects=False)
fetchUrl = response.headers['Location']
reverseUrl = fetchUrl.replace("http:", "https:") + '&q=e621&oq=e621&gs_1='
print "going to:\n\n" + reverseUrl + "\n\n"

e621_link = requests.get(reverseUrl, allow_redirects=True)
if response.history: print "there were redirects"
soup = BeautifulSoup(e621_link.text.encode('utf-8'), 'html.parser')

outfile = open('output.html', 'w').write(soup.prettify().encode('utf-8'))

#for data in soup.find_all("a"):
#        print data

#for data in soup.find_all("a", attrs={'data-cthref' : True}):
#        print data:w
        
