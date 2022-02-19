# Web scrapper of bowie lyrics

This repository contains my final project for the "Python for Everybody Specialization" from coursera. Here you will find the code I wrote to scrappe all David Bowie's Lyrics using BeautifulSoup, and count the unique words per song, creating a data base with sqllite in the process to store all the data gathered.

I have divided the process into three different scripts, in order to make it more efficient.

1 - The first one, named "Initial Scrape", takes all the song names of the page www.lyrics.com and the links to their lyrics and place them in a Data Base called dbowie.sqlite.

2 - The second one goes link by link collecting the lyrics for all the songs of the data base, and counting the words used by David Bowie in his songs, to give the main 10 words.


The result of this project was:

[('down', 1114),
 ('little', 1126),
 ("don't", 1245),
 ('with', 1251),
 ('dance', 1302),
 ('like', 1335),
 ('that', 1477),
 ("it's", 1698),
 ('love', 1795),
 ('your', 2515)]

