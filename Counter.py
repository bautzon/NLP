import nltk,re
from nltk.corpus import twitter_samples
from collections import Counter
nltk.download('twitter_samples')

all_positive_tweets = twitter_samples.strings('positive_tweets.json')
all_negative_tweets = twitter_samples.strings('negative_tweets.json')

all_positive_tweets[0:10]

newtext = all_positive_tweets[0:100]
from Cleaner import * 

#print (newtext)
print(len(newtext))

positive_counts = Counter()
negative_counts = Counter()
total_counts = Counter()

for i in range(len(all_positive_tweets)):
    for word in all_positive_tweets[i].lower().split(" "):
        positive_counts[word]+=1
        total_counts[word]+=1
 
 
for i in range(len(all_negative_tweets)):
    for word in all_negative_tweets[i].lower().split(" "):
        negative_counts[word]+=1
        total_counts[word]+=1

#print(positive_counts.most_common()[0:10])
#print(positive_counts.most_common()[0:10])