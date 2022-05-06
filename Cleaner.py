from cgitb import text
from lib2to3.pgen2 import token
from ntpath import join
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.util import ngrams
from nltk.lm import NgramCounter
from Scraper import *
import re

clean=[]
 
def remove_regex(scraped_data):
    print("CLEANING DATA")
    for dirty in scraped_data:
    #for list_to_clean in data["title"]
        prelim_cleaner = re.sub("\d+","",dirty).lower()
        string_clean = re.sub("(&amp;|[^\w\d\s\-'´`@’”“\"]+|(?<!\w)rt(?!\w)|\s#\S+|http.*?(?=\s)|ftp|([A-Za-z0-9]+[-._])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+)", "", prelim_cleaner) #Email regex from: https://stackabuse.com/python-validate-email-address-with-regular-expressions-regex/
        clean.append(string_clean)
        
    return clean    
     
tokenized = word_tokenize(clean)
data_bigrams = ngrams(tokenized, 4)

#cleaner og tokenizer tekstinput (string)

"""
#cleaner elementer af liste og returnerer cleaned liste
def cleaner(data): 
    clean=[]
    
    regex_cleaned_string = remove_regex(data)         
    #cleaned=re.sub("\W +", ' ',regex_cleaned_string).lower()
    #tokenized=word_tokenize(cleaned)
    #stemmer= PorterStemmer()
    clean.append(regex_cleaned_string)
    clean_text_string=" ".join(clean)
    print(clean)
    return clean
"""
def print_cleaned_data(clean):
    if clean:
        for i in clean:
            print(i)
    else:
        print("No data stored. Did you scrape the data first?")  

