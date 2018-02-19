import matplotlib
import requests
from bs4 import BeautifulSoup
from jedi.refactoring import inline

url = 'http://course.fast.ai/lessons/lesson1.html'
url=input()
r = requests.get(url)
type(r)
data=r.text
soup=BeautifulSoup(data,"html")
type(soup)
text=soup.get_text()
import nltk
# Get English stopwords and print some of them
#nltk.download('stopwords')
sw = nltk.corpus.stopwords.words('english')
s=sw[:5]

import re
text=soup.get_text()
words=[]
tokens = re.findall('\w+', text)
for word in tokens:
    if word not in sw:
        words.append(word)
print(words[:8])
print (s)

#Import datavis libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Figures inline and set visualization style
#%matplotlib inline
sns.set()

# Create freq dist and plot
freqdist1 = nltk.FreqDist(words)
freqdist1.plot(25)
