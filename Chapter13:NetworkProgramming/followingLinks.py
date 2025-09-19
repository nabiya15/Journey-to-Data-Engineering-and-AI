# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# or pip install beautifulsoup4 to ensure you have the latest version
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl # defauts to certicate verification and most secure protocol (now TLS)

# Ignore SSL/TLS certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

position = int(input('Enter position: '))
count = int(input('Enter the number of times to repeat the cycle: '))
url = 'http://py4e-data.dr-chuck.net/known_by_Danikah.html'

for i in range(count+1):
    html = urllib.request.urlopen(url, context=ctx).read()
    print('Retrieving:', url)
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    url = tags[position-1].get('href', None)

    #print(tag.get('href', None), i)
    # for i, tag in enumerate(tags):
    # if i == position:
    #     url = tag.get('href', None)
    #     print(url)
    #     break