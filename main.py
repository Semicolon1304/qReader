#Import all the things
from bs4 import BeautifulSoup
import urllib3
import requests

#Reading the queue data
url = 'https://2b2t.io/api/queue?last=true'
page = requests.get(url)

#Did the page download?
if page.status_code == 200:
    print('Working!')
else :
    print("Something went wrong with downloading the page. Don't ask me how to fix it because IDK")


