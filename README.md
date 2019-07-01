# flairwars-graph
Uses matplotlib and pushshift to plot the amount of posts on /r/flairwars and associated subreddits

scraper.py accesses the pushshift API through the psaw module to put daily post counts in data.txt. This is appended for every day in case the program crashes before all the data can be written. If the program reaches the end without crashing, all the data is put in dataFinal.txt as a long array.

grapher.py imports dataFinal.txt, converts it back to an array and plots it with matplotlib. 

![Graph](https://github.com/uood5/flairwars-graph/blob/master/graph.png)
