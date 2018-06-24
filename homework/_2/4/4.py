import nltk
nltk.download('punkt')
from nltk import *



def splitSentence(paragraph):
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    sentences = tokenizer.tokenize(paragraph)
    return sentences


def wordtokenizer(sentence):
    words = nltk.WordPunctTokenizer().tokenize(sentence)
    return words


f = open("A.txt");
count = {}
for l in f:
    sentences = splitSentence(l)
    words = wordtokenizer(sentences)
    print(words)