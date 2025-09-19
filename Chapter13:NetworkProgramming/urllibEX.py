import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = {}
# reads the file
for line in fhand:
    print(line.decode().rstrip())

# lets count the words in the file 
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0)+1
print(counts)