from sympy import source
import spacy
from nltk import Tree3
from Scraper import *
from Cleaner import *
from Stemmer import *
from Counter import *

def choose_method():
    print("""
    Welcome - Choose an option
    1) Scrape from link
    2) Scrape from subreddit
    3) Scrape from twitter hashtag
    4) Print data
    5) Quit
    6) Save to file
    7) print tree
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
        elif userinput=="7":
            make_tree()  
        else:
            print("Unable to understand")


choose_method()   #scraper
cleaned_text_list=cleaner(data['title'])[0]
cleaned_text_string=cleaner(data['title'])[1]
   
