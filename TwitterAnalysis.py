from cgitb import text
import spacy
from nltk import Tree
from spacy.symbols import *
from Scraper import *
#from nltk.corpus import twitter_samples

#all_positive_tweets = twitter_samples.strings('positive_tweets.json')
#all_negative_tweets = twitter_samples.strings('negative_tweets.json')

test_text="Autonomous cars drives insurance liability toward manufacturers"
nlp = spacy.load("en_core_web_sm")

def search_orgs(text):
    doc=nlp(text)
    ent_list=[]
    for entity in doc.ents:
        if entity.label_=="ORG" or "PERSON" or "MONEY":
            ent_list.append(entity.text)
    return ent_list        

def check_org_for_POS_head(text,POS):
    ent_list=search_orgs(text)
    #print(ent_list)
    adjectives=set()
    doc=nlp(text)
    for token in doc:
        #token.text in ent_list and 
        if token.head.pos == POS and token.text in ent_list: 
            adjectives.add(token.head)
            print(f' ADJ  connected to {token.text} are {adjectives}')
            #Give points if true.
data=data["title"]

for tweet in data:
    check_org_for_POS_head(tweet,VERB)
    check_org_for_POS_head(tweet, ADJ)
print (data)
"""
def to_nltk_tree(node,source=None):

   if node.n_lefts + node.n_rights > 0:
     parsed_child_nodes = [to_nltk_tree(child) for child in node.children]
     return Tree(node.orth_, parsed_child_nodes)
   else:
     return node.orth_
  
    
dependency_parser = spacy.load("en_core_web_sm")
my_parsed_sentence = dependency_parser(te)

for sent in my_parsed_sentence.sents:
    to_nltk_tree(sent.root).pretty_print()



visited=[]
def dfs(node):
    visited.append(node.text)
    if not node.children:
        return []
    for child in node.children:
        dfs(node)
    print(visited)    



"""