import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode= ssl.CERT_NONE


url = 'https://www.harvestgreentexas.com/homes'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

#retrieve all a tags
atags = soup('a')

# for tag in atags:
#     print(tag.get('src', None))
print(soup.prettify())

