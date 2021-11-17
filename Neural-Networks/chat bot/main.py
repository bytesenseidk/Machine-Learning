import nltk
import numpy
import tflearn
import tensorflow
import random
import json
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

with open("intents.json") as file:
    data = json.load(file)
    print(data)