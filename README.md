# Web scrapper of bowie lyrics

This repository contains my final project for the "Python for Everybody Specialization" from coursera. Here you will find the code I wrote to scrappe all David Bowie's Lyrics using BeautifulSoup, and count the unique words per song, creating a data base with sqllite in the process to store all the data gathered.

I have divided the process into three different scripts, in order to make it more efficient.

1 - The first one, named "Initial Scrape", takes all the song names of the page www.lyrics.com and the links to their lyrics and place them in a Data Base called dbowie.sqlite.
2 - The second one goes link by link collecting the lyrics for all the songs of the data base.
3 - Finally, the last script counts the words used by Bowie and make a Word Cloud with D3.js library.

