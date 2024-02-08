from nltk.tokenize import word_tokenize, sent_tokenize
from collections import Counter
import matplotlib.pyplot as plt
from math import log
import numpy as np

with open('kjv.txt', 'r') as f:
    text = f.read()
    text = text.replace('\n', ' ')
    text += ' '

with open('jungle.txt', 'r') as f:
    text += f.read()

sentences = sent_tokenize(text)
words = [w for s in sentences for w in word_tokenize(s)]

words = [w.lower() for w in words if w.isalpha()]


lengths = [len(w) for w in words]


hist = Counter(lengths)

def words_of_length(n):
    return set([w for w in words if len(w) == n])

print(words_of_length(1))
print(words_of_length(2))
print(words_of_length(3))


plt.bar(range(1, 19), [hist[i] for i in range(1, 19)])


plt.bar([log(x) for x in range(1, 19)], [log(hist[i]) for i in range(1, 19)])

rho = np.corrcoef(range(2, 19), [hist[i] for i in range(2, 19)])[0, 1]