# Import Library
import time, threading
from pydub import AudioSegment
from pydub.playback import play
from bs4 import BeautifulSoup
import requests

sound = AudioSegment.from_file("airRaid.wav")

#Reading the queue data
page = requests.get('https://2b2t.io/api/queue?last=true')
soup = BeautifulSoup(page.text, 'html.parser')
#Did the page download?
if page.status_code == 200:
    print('Working!')
else :
    print("Something went wrong with downloading the page. Probably too many requests. try again later.")

#declaring this function thing
def refresh() :
        page = requests.get('https://2b2t.io/api/queue?last=true')
        soup - BeautifulSoup(page.text, 'html.parser')
        fullQ = (soup.prettify())
        uselessCrapVar, almost = fullQ.split(',')
        queuing = almost[0:-3]
        queue = int(queuing)
        print(queue)
        

# obtaining data and storing in var 'queue'
fullQ = (soup.prettify())
uselessCrapVar, almost = fullQ.split(',')
queuing = almost[0:-3]
queue = int(queuing)
print(queue)
queue = 20




# Wow figuring that out sucked. Almost done. End of 5/16/20

# If/Else crap time
if queue <= 20:
    play(sound)

else:
    while queue > 20:
        time.sleep(60)
        page = requests.get('https://2b2t.io/api/queue?last=true')
        soup = BeautifulSoup(page.text, 'html.parser')
        fullQ = (soup.prettify())
        uselessCrapVar, almost = fullQ.split(',')
        queuing = almost[0:-3]
        queue = int(queuing)
        print(queue)


    