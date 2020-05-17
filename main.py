# Import all the things
import pydub
from pydub import AudioSegment
from pydub.playback import play
from bs4 import BeautifulSoup
import urllib3
import requests


airRaid = AudioSegment.from_wav("airRaid.wav")
#Reading the queue data
url = 'https://2b2t.io/api/queue?last=true'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
#Did the page download?
if page.status_code == 200:
    print('Working!')
else :
    print("Something went wrong with downloading the page. Probably too many requests. try again later.")


# obtaining data and storing in var 'queue'
fullQ = (soup.prettify())
uselessCrapVar, almost = fullQ.split(',')
queuing = almost[0:-3]
queue = int(queuing)
print(queue)




# Wow figuring that out sucked. Almost done. End of 5/16/20

# If/Else crap time
if queue <= 20:
    play(airRaid)

else:
    while queue > 20:
        page = requests.get(url)
        fullQ = (soup.prettify())
        uselessCrapVar, almost = fullQ.split(',')
        queuing = almost[0:-3]
        queue = int(queuing)
        print(queue)

    


    
    




