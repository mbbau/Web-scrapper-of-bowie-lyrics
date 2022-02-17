# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 16:24:21 2022

@author: matiasb
"""

import sqlite3
import urllib.error
import ssl
from urllib.parse import urljoin
from urllib.parse import urlparse
from urllib.request import urlopen
from bs4 import BeautifulSoup

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

conn = sqlite3.connect('dbowie.sqlite')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Tracks
    (id INTEGER PRIMARY KEY, track TEXT UNIQUE, url TEXT UNIQUE, lyric TEXT UNIQUE)''')

url = "https://www.lyrics.com/artist/David-Bowie/3753"
lyrics_page = urllib.request.urlopen(url, context=ctx)

soup = BeautifulSoup(lyrics_page, "html.parser")

# with this print, I saw the main structure of the html and found out that I need to 
# look for the tag named a with the href and the text within it. In there I will find
# the name of the song and a link to its lyric.
#print(soup.prettify())
# list_of_tags = list()
# for tag in soup.find_all(True):
#     list_of_tags.append(tag.name)

tags = soup('a')
songs = dict()

for tag in tags:
    link = tag.get('href')
    if "David+Bowie" not in link: continue
    song = tag.text
    songs[song] = link
    cur.execute('INSERT OR IGNORE INTO Tracks (track, url) VALUES ( ?, ? )', ( song, link, ) )
conn.commit()


