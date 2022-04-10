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

#cleaner og tokenizer tekstinput (string)


#cleaner elementer af liste og returnerer cleaned liste
def cleaner(text):           
    stringify=",".join(text)
    cleaned=re.sub("\W +", ' ',stringify).lower()
    tokenized=word_tokenize(cleaned)
    stemmer= PorterStemmer()
    c_text =[stemmer.stem(token) for token in tokenized]
    c_text_string=" ".join(c_text)

    
    return c_text,c_text_string

