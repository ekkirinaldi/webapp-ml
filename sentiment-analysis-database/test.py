from wordcloud import WordCloud, STOPWORDS
import os
import tweepy
import csv
import re
import matplotlib.pyplot as plt


#print(csv.reader('result.csv'))
file = open('result.csv')
csvreader = csv.reader(file)
print(csvreader)

rows =' '
for row in csvreader:
    rows += ' '+ str(row)

#pattern = r'[^A-Za-z0-9]+'
#sample_str = re.sub(pattern, '', rows)

#regex = re.compile('[^a-zA-Z]')
#rows = regex.sub('', rows)

STOPWORDS = ["https", "co", "RT", ] + list(STOPWORDS)

wordcloud = WordCloud(width= 800, height = 600, random_state=1, background_color='salmon', colormap='Pastel1', collocations=False, stopwords = STOPWORDS).generate(rows)
wordcloud.to_file('cloud.png')

plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)
 
plt.show()