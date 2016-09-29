import requests
import time
import re

from bs4 import BeautifulSoup
result = requests.get("http://kroq.cbslocal.com/playlist/")

c = result.content
filename = time.strftime("%Y-%m-%d-%H-%M")
soup = BeautifulSoup(c, "lxml")

track = [div.text for div in soup.findAll('div', attrs={'class': 'track-title'})]

for t in track:
	with open('playlist-' + filename + '.txt', 'a') as f:
		tracktitle = str(t)
		cleantitle1 = tracktitle.replace("\n\t\t\t\t\t\t\t\t\t\t\t", "")
		cleantitle2 = cleantitle1.replace("\t\t\t\t\t\t\t\t\t\t", "")
		f.write(cleantitle2)
		f.write("\n")

time.sleep(10)		
from gmusicapi import Mobileclient
import sys

api = Mobileclient()
logged_in = api.login('username', 'password', '1234567890abcdef', 'en-US')

plist = 'playlist-id'
s = open('playlist-' + filename + '.txt', 'r')
for line in s:
	trackinfo = str(line)
	songsearch = api.search(trackinfo, max_results=1)
	for item in songsearch['song_hits']:
		print (item["track"]['nid'])
	track = str(item["track"]['nid'])
	time.sleep(1)
	addplist = api.add_songs_to_playlist((plist), (track))