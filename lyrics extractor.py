# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 08:14:28 2022

@author: matiasb
"""

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
import zlib
import string
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

conn = sqlite3.connect('dbowie.sqlite')
cur = conn.cursor()

# I will inspect where the lyrics are in every link by analyzing the html file
# url2 = "https://www.lyrics.com/lyric/35488143/David+Bowie/Ashes+to+Ashes"
# song_page = urllib.request.urlopen(url2, context=ctx)
# second_soup = BeautifulSoup(song_page, 'html.parser')
# print(second_soup.prettify())
# list_of_tags_two = list()
# for tag in second_soup.find_all(True):
#       list_of_tags_two.append(tag.name)
# print(second_soup.pre.text)
# the lyrics are under the <pre> tag!

cur.execute('SELECT url FROM Tracks')
webs = list()
songs = list()
for row in cur:
    webs.append(str(row[0]))
for link in webs:
    try:
        new_url = "https://www.lyrics.com" + link
        song_page = urllib.request.urlopen(new_url, context=ctx)
        second_soup = BeautifulSoup(song_page, 'html.parser')    
        song_lyric = second_soup.pre.text
        song = song_lyric.strip()
        song = song.lower()
        song = song.replace("\n"," ")
        song = song.replace(","," ")
        song = song.replace("(","")
        song = song.replace(")","")
        song = song.replace("\r"," ")
        song = song.replace("'"," ")
        songs.append(song) 
    except:
        continue

counts = dict()
for song in songs:    
    song_lyric = song.strip()
    song_lyric = song_lyric.lower()
    words = song_lyric.split()
    for word in words:
        if len(word) < 4 : continue
        counts[word] = counts.get(word,0) + 1

x = sorted(counts, key=counts.get, reverse=True)
highest = None
lowest = None
for k in x[:100]:
    if highest is None or highest < counts[k] :
        highest = counts[k]
    if lowest is None or lowest > counts[k] :
        lowest = counts[k]
print('Range of counts:',highest,lowest)

# here i will visualize the data using some code from:
#  "Python for everybody specialization"
# in order to make a word cloud

# Spread the font sizes across 20-100 based on the count
bigsize = 80
smallsize = 20

fhand = open('gword.js','w')
fhand.write("gword = [")
first = True
for k in x[:100]:
    if not first : fhand.write( ",\n")
    first = False
    size = counts[k]
    size = (size - lowest) / float(highest - lowest)
    size = int((size * bigsize) + smallsize)
    fhand.write("{text: '"+k+"', size: "+str(size)+"}")
fhand.write( "\n];\n")
fhand.close()

print("Output written to gword.js")
print("Open gword.htm in a browser to see the vizualization")

sorted_words = sorted(counts.items(), key=lambda kv: kv[1])

# Generate word cloud
wordcloud = WordCloud(width= 3000, height = 2000, random_state=1, background_color='salmon', colormap='Pastel1', collocations=False, stopwords = STOPWORDS).generate_from_frequencies(counts)

# Plot
plt.figure(figsize=(15,8))
plt.imshow(wordcloud)
