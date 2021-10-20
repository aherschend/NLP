from nltk.corpus import stopwords
from textblob import TextBlob
import nltk
from pathlib import Path
#import pandas as pd


#nltk.download('stopwords')

from nltk.corpus import stopwords

blob = TextBlob("Today is a beautiful day.")

print(blob.words)

cleanlist = [word for word in blob.words if word not in stops]

print(cleanlist)

blob = TextBlob(Path('RomeoandJuliet.txt').read_text())

print(blob.words.count("joy"))

print(blob.word_counts["juliet"])

print(blob.noun_phrases.count("lady capulet"))

print(blob.words.count('thou'))


print(items)

clean_items = [i for i in items if i[0] not in stops]

print(clean_items[:10])