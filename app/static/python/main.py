import json
from datetime import datetime
import time
from js import document, window, setInterval, console

from pyodide import create_proxy

# Create a Python proxy for the callback function

class Countdown:

    def __init__(self):
        time = document.getElementById("time").value
        mins = int(time.split(':')[0].strip())
        secs = int(time.split(':')[1].strip())
        self.total_time = (mins*60) + secs
        self.time_remaining = self.total_time
        self.pause = False
        document.getElementByID("total_time").innerHTML = timer = f'{mins:02d}:{secs:02d}'
        document.getElementByID("start").onclick(start_proxy)
        document.getElementByID("stop").onclick(reset_proxy)
        document.getElementByID("reset").onclick(reset_proxy)

    def update_time_remaining(self, mins, secs=0):
        self.time_remaining = (mins*60) + secs

    def start_countdown(self):
        now = datetime.now()
        while self.time_remaining:
            if not self.paused:
                diff = datetime.now() - now
                mins -= diff.seconds // 60
                secs = diff.seconds
                ms = diff.microseconds
                self.update_time_remaining(mins, sec)
            timer = f'{mins:02d}:{secs:02d}:{ms:03d}'
            document.getElementsByID("timer").innerHTML = timer
            

countdown = Countdown()


def start(e=None):
    not e or e.preventDefault()
    countdown.paused = False
    countdown.start_countdown()
start_proxy = create_proxy(start)

def reset(e=None):
    not e or e.preventDefault()
    
    countdown.time_remaining = self.total_time
    countdown.paused = True
reset_proxy = create_proxy(reset)
    
def pause(e=None):
    not e or e.preventDefault()
    countdown.paused = True
pause_proxy = create_proxy(pause)
        