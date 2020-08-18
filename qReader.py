from contextlib import contextmanager
import time, threading
#Time Crap

from bs4 import BeautifulSoup
#Allows HTML import
import requests
import sys, os
#Also HTML import(?)

@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:  
            yield
        finally:
            sys.stdout = old_stdout
with suppress_stdout () :
    from pydub import AudioSegment
    from pydub.playback import play
#Allows audio
    sound = AudioSegment.from_file('sound.wav')

#Reading the queue data
page = requests.get('https://2b2t.io/api/queue?last=true')
soup = BeautifulSoup(page.text, 'html.parser')
#Did the page download?
if page.status_code == 200:
    print('Working!')
else :
    print("Something went wrong with reading the queue data. Probably too many requests. try again later.")

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


    
        

    


    
    






# %%
