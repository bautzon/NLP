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
 
def remove_regex(scraped_data):
    #for list_to_clean in data["title"]
    stringify=",".join(scraped_data)
    string_clean = re.sub("(@|//|#|http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])", "",stringify)
    print(string_clean)
    return string_clean

#cleaner og tokenizer tekstinput (string)


#cleaner elementer af liste og returnerer cleaned liste
def cleaner(dict_to_clean):  
    regex_cleaned_string = remove_regex(dict_to_clean["title"])         
    cleaned=re.sub("\W +", ' ',regex_cleaned_string).lower()
    tokenized=word_tokenize(cleaned)
    stemmer= PorterStemmer()
    raw_text =[stemmer.stem(token) for token in tokenized]
    clean_text_string=" ".join(raw_text)

    return raw_text,clean_text_string

def print_cleaned_data(raw_text):
    if raw_text:
        clean_text = cleaner(raw_text)
        print("Printing Data:")
        print(clean_text)
    else:
        print("No data stored. Did you scrape the data first?")  

