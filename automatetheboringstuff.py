"""import time
for i in range (3):
    print 'tick'
    time.sleep(1)
    print 'tock'
    time.sleep(1)

    
somnetFile = open('somnet29.txt')
somnetFile.readlines()
print somnetFile


import time
fh = open('somnet29.txt','r')
for lines in fh:
    print lines
    
  

import time
for i in range (1):
    print 'hello peter'
    time.sleep(2)
    print 'you are the best'
    time.sleep(2)
    print 'it is time to say goodbye'
    time.sleep(2)
print 'the end'

the_answer = 3+5
print the_answer

word1 = 'spreadsheets'
word2 = 'are'
word3 = 'cool'

truth = word1 + " "+ word2 + " " + word3
print truth


import webbrowser
webbrowser.open('http://inventwithpython.com/')



import webbrowser
webbrowser.open('http://coursera.org/')


#http://docs.python-requests.org/en/latest/user/install/#get-the-code
import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
type(res)
res.status_code == requests.codes.ok
len(res.text)
print(res.text[:250])


import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
    
import requests, bs4
res = requests.get('http://nostarch.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text)
type(noStarchSoup)

 
import requests, bs4
exampleFile = open('team.html')
exampleSoup = bs4.BeautifulSoup(exampleFile)
type(exampleSoup)


import bs4
exampleFile = open('team.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read())
elems = exampleSoup.select('#author')
type(elems)
#<class 'list'>
len(elems)
type(elems[0])
#<class 'bs4.element.Tag'>
elems[0].getText()
'Al Sweigart'
str(elems[0])
#'<span id="author">Al Sweigart</span>'
 elems[0].attrs
{'id': 'author'}
pElems = exampleSoup.select('p')
str(pElems[0])

 
from bs4 import BeautifulSoup
import urllib
r = urllib.urlopen('http://www.aflcio.org/Legislation-and-Politics/Legislative-Alerts').read()
soup = BeautifulSoup(r)
print type(soup)
print soup.prettify()[0:1000]

from IPython.display import Image
Image('http://www.openbookproject.net/tutorials/getdown/css/images/lesson4/HTMLDOMTree.png')

 """ 
http://web.stanford.edu/~zlotnick/TextAsData/Web_Scraping_with_Beautiful_Soup.html
import os, csv
os.chdir("/Users/anitaowens/Documents/pythonpractice/")

with open("lobbying.csv", "w") as toWrite:
    writer = csv.writer(toWrite, delimiter=",")
    writer.writerow(["name", "link", "date"])
    for a in lobbying.keys():
        writer.writerow([a.encode("utf-8"), lobbying[a]["link"], lobbying[a]["date"]])