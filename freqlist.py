from nltk.book import *

fdist = FreqDist(text1)
for word in fdist:
    if len(word) == 4:
        print(word + " ---> " + str(fdist[word]))
