import urllib.error
import ssl
import urllib.request, urllib.parse, urllib.error
from urllib.parse import urljoin
from urllib.parse import urlparse
from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def format(starturl):
    if ( len(starturl) < 1 ) : starturl = 'http://www.dr-chuck.com/'
    if ( starturl.endswith('/') ) : starturl = starturl[:-1]
    if ( starturl.endswith('.htm') or starturl.endswith('.html') ) :
        pos = starturl.rfind('/')
        starturl = starturl[:pos] 
        return(starturl)

def retrive(url):
    link=list()
    document = urllib.request.urlopen(url, context=ctx)
    html = document.read()
    print('('+str(len(html))+')', end=' ')
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    count = 0
    for tag in tags:
        href = tag.get('href', None)
        if (href is None ) : continue
        # Resolve relative references like href="/contact"
        up = urlparse(href)
        if ( len(up.scheme) < 1 ) :
            href = urljoin(url, href)
        ipos = href.find('#')
        if ( ipos > 1 ) : href = href[:ipos]
        if ( href.endswith('.png') or href.endswith('.jpg') or href.endswith('.gif') ) : continue
        if ( href.endswith('/') ) : href = href[:-1]
        link.append(href)
    print(link)
    posn =int(input("Enter the posn for follow:"))
    return(link[posn])
url = input('Enter web url or enter: ')
while True:
    url=retrive(url)
