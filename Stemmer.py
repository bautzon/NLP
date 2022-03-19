import spacy
from nltk import Tree


def file_to_string(file):
    with open ("demofile.txt", "r",encoding="utf-8") as f:
        data=f.readlines()
        print(data)
    datastring=''.join(data)
    return datastring


dependency_parser = spacy.load("en_core_web_sm")
my_parsed_sentence = dependency_parser(datastring)

def to_nltk_tree(node):
  if node.n_lefts + node.n_rights > 0:
    parsed_child_nodes = [to_nltk_tree(child) for child in node.children]
    return Tree(node.orth_, parsed_child_nodes)
  else:
    return node.orth_
  
for sent in my_parsed_sentence.sents:
 to_nltk_tree(sent.root).pretty_print()

to_nltk_tree(f)


