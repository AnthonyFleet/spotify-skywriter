#! /usr/bin/python

import sys
import spotipy
import spotipy.util as util

scope = 'user-modify-playback-state'
username = 'anthonyfleet'
token = util.prompt_for_user_token(username, scope, client_id='<insert client ID',client_secret='<insert client secret',redirect_uri='http://localhost/')


if token:
  sp = spotipy.Spotify(auth=token)
  sp.previous_track()

else:
   print ("Can't get token for", username)
