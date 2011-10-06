from BeautifulSoup import BeautifulStoneSoup, BeautifulSoup, Comment
import urllib
import os
import shutil

def scrape():
    try:
        p = open('save/dip.html', 'r')
        soup = BeautifulSoup(p.read())
    except IOError, e:
        return None
    
    for i in soup.findAll('a'):
        if i.has_key('href'):
            if i['href'][0:4] == 'http':
                try:
                    page = urllib.urlopen(i['href']).read()
                    filename = i['href'].split('/')[-2] + '/' + i['href'].split('/')[-1]
                    if not os.path.exists(i['href'].split('/')[-2]):
                        os.mkdir(i['href'].split('/')[-2])
                    with open(filename, 'w') as out:
                        out.write(soup.renderContents())
                except IOError, e:
                    pass
def purify(filename):
    with open(filename, 'r') as f:
        soup = BeautifulSoup(f)
    for div in soup.findAll('div'):
        if div.has_key('id'):
            if div['id'] == 'wm-ipp':
                div.extract()
    for script in soup.findAll('script'):
        script.extract()
    for comment in soup.findAll(text=lambda text:isinstance(text, Comment)):
        comment.extract() 
    for link in soup.findAll('link'):
        if link.has_key('rel'):
            if link['rel'] == "home":
                link['href'] == "http://diveinpython.org/"
            if link['rel'] == "stylesheet":
                link['href'] == "/css/diveintopython.css"
            
    new_soup = BeautifulSoup(soup.renderContents())
    for i in new_soup.findAll('a'):
        if i.has_key('href'):
            if i['href'][0:4] == 'http':
                print i['href']
    with open(filename, 'w') as out:
        out.write(new_soup.renderContents())
if __name__ == '__main__':
    #for f in os.listdir('/home/josh/programming/diveintopython/'):
        #if ".html" in f.name:
            #purify(f)
    
    purify('redhat.html')
    
    