from urllib.error import HTTPError
import tweepy
import requests
import json
import urllib.request


data= {"title":[],
              "body":[],
              "upvotes":[]   
      }


def scrape_twitter(hashtag):
    bearer="AAAAAAAAAAAAAAAAAAAAAOD9ZwEAAAAAp5wAOHyavG6WIsJL7dmJEmclxO8%3DBw19697vkBcRxoEI5gRfiVCMiAoVSvXxYtWI48qI5lLvlqO8Zw"
    secret="t1HgnfQceyiviACoLBVeZ5mhVzwoVSGJrmHDvzznMOUdQu3uRX"
    api="SZPsGj9Ixdrfy1nhv6TzuzMbE"
    client=tweepy.Client(bearer_token=bearer)
    response=client.search_recent_tweets(query=hashtag,max_results=10,tweet_fields=['lang','text','public_metrics'],expansions=['author_id'])
    if response.data:
        print(f"Adding tweets regarding #{hashtag} ")
        for tweets in response.data:
            if tweets is not None and tweets.lang=="en":
                data['title'].append(tweets.text)
    else: 
        print(f"unable to find anything for #{hashtag}")            


def scrape_subrreddit(subreddit):
  try:
    source2 = urllib.request.urlopen(subreddit).read()
    jsonResponse = json.loads(source2.decode('utf-8'))
    print(f"Adding content from /r/{subreddit} to dict")
    for i in jsonResponse['data']['children']:
        upvotes=i['data']['ups']
        title=i['data']['title']
        body=i['data']['selftext']
        if upvotes>50:
            data['title'].append(title)
            data['body'].append(body) 
            data['upvotes'].append(upvotes)    
  except HTTPError as e:
      print(f"Fejl: {e}")


def print_scraped_data():
    if data:
        print("Printing Data:")
        print(data)
    else:
        print("No data stored. Did you scrape the data first?")    



def determine_link():
    url=input("Skriv et link til et subreddit eller til et twitter hashtag ")
    if "reddit" in url:
         scrape_subrreddit(url+".json?limit=10")
    elif "twitter" in url:
        hashtag=url.split("/")[-1][:-1]     #Extracting hashtag
        scrape_twitter(hashtag)


def choose_method():
    print("""
    Welcome - Choose an option
    1) Scrape from link
    2) Scrape from subreddit
    3) Scrape from twitter hashtag
    4) Print data
    5) Quit
    6) Save to file
    """)
    quit=False
    while quit == False:
        userinput=input("Write choice ")
        if userinput=="1":
            determine_link()
        elif userinput=="2":
            subredditinput=input("Write a subreddit name ")
            scrape_subrreddit("https://www.reddit.com/r/"+subredditinput+".json?limit=10")
        elif userinput=="3":
            twitterinput=input("Write a topic to search twitter ")
            scrape_twitter(twitterinput)
        elif userinput=="4":
            print_scraped_data()
        elif userinput=="5":
            quit=True
        elif userinput=="6":
            save_to_txt()
        else:
            print("Unable to understand")




def save_to_txt():
    f = open("demofile.txt", "w",encoding="utf-8")
    for i in data['title']:
        f.write(i)




