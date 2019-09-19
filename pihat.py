#!/usr/bin/env python
import skywriter
import signal
import subprocess

@skywriter.flick()
def flick(start,finish):
  print('Got a flick!', start, finish)
  

  if start == 'east':
    subprocess.call ("/home/pi/spotify-jedi/spotify-skywriter/skip_forward.py")

  if start == 'west':
    subprocess.call ("/home/pi/spotify-jedi/spotify-skywriter/skip_back.py")

signal.pause()
