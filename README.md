# spotify-skywriter

Install spotipy
(Had to manually copy client.py file from github as the pip install method appears to be missing some functions, including user playback).

Set up client ID and secret using spotify developer portal.

Use client ID and secret to generate token with spotipy. This will also generate a hidden file called cache-<username>. 
This hidden file contains a refresh token that can be used to automatically connect to your spotify account without manual intervention. 

Set up service file called pihat.service to run python script as a service.
(didn't work until added WorkingDirectory as it couldn't find cache file at relative path)

 [Unit]
 Description=PiHat
 After=multi-user.target

 [Service]
 Type=idle
 ExecStart=/usr/bin/python /home/pi/spotify-jedi/spotify-skywriter/pihat.py
 User=pi
 PWD=/home/pi/spotify-jedi/spotify-skywriter
 WorkingDirectory=/home/pi/spotify-jedi/spotify-skywriter


 [Install]
 WantedBy=multi-user.target
