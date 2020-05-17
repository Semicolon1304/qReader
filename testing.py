#Import all the things
from playsound import playsound
from bs4 import BeautifulSoup
import urllib3
import requests


#Reading the queue data
url = 'https://2b2t.io/api/queue?last=true'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
#Did the page download?
if page.status_code == 200:
    print('Working!')
else :
    print("Something went wrong with downloading the page. Don't ask me how to fix it because IDK")



#obtaining data and storing in var 'queue'
fullQ = (soup.prettify())
uselessCrapVar, almost = fullQ.split(',')
queue = almost[0:-3]
print(queue)
