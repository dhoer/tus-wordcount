import urllib
import collections
import re
import sys
from bs4 import BeautifulSoup

url = sys.argv[1]
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, features="lxml")

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()

words = {}

for line in text.splitlines():
    for word in line.split():
        w = re.sub('[!@#$:"\.&\'0-9\-,]', '', word)
        if w in words:
            words[w] = words[w] + 1
        else:
            words[w] = 1

del words['']

for w in collections.OrderedDict(sorted(words.items())):
    count = words[w]
    print w, count


print("\nWord count: %d" % len(words))
