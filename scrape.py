from BeautifulSoup import BeautifulStoneSoup, BeautifulSoup, Comment
import urllib
import os
import shutil
import string
import re

URL='http://www.diveintopython.net/'

def scrape():
    try:
        p = open('save/dip.html', 'r')
        soup = BeautifulSoup(p.read())
    except IOError, e:
        print "io error code: %d msg: %s" % (e.returncode, e.message)
        return None
    
    for i in soup.findAll('a'):
        if i.has_key('href'):
            if i['href'][0:4] == 'http' and '#' not in i['href']:
                try:
                    filename = i['href'].split('/')[-2] + '/' + i['href'].split('/')[-1]
                    print "saving %s into %s" % (i['href'], filename, )
                    if not os.path.exists(i['href'].split('/')[-2]):
                        os.mkdir(i['href'].split('/')[-2])
                    with open(filename, 'w') as out:
                        out.write(urllib.urlopen(i['href']).read())
                except IOError, e:
                    pass
def purify(filename):
    
    with open(filename, 'r') as f:
        
        soup = BeautifulSoup(f)
    print "working on %s" % (filename, )
    for div in soup.findAll('div'):
        if div.has_key('id'):
            if div['id'] == 'wm-ipp':
                div.extract()
    for script in soup.findAll('script'):
        script.extract()
    for comment in soup.findAll(text=lambda text:isinstance(text, Comment)):
        comment.extract() 
    for link in soup.findAll('link'):
        if link.has_key('rev'):
            if link['rev'] == 'made':
                link['href'] == 'josh@servercobra.com'  
        if link.has_key('rel'):
            if link['rel'] == "home":
                link['href'] = URL
            if link['rel'] == "stylesheet":
                link['href'] = "/css/diveintopython.css"
            if link['rel'] == "next":
                link['href'] = URL + '/'.join(link['href'].split('/')[8:])
        
    for a in soup.findAll('a'):
        if a.has_key('href'):
            if 'http://web.archive.org/' in a['href']:
                print "print cleaning up link: %s" % (a['href'])
                a['href'] = URL + '/'.join(a['href'].split('/')[8:])
               
                #a['href'] = 'http://www.diveintopython.net/' a['href'].split('/')[8:]
            #if 'http://diveintopython.net/' in a['href']:
    for form in soup.findAll('form'):
        if form.has_key('action'):
            if 'http://web.archive.org/' in form['action']:
                form['action'] = 'http://www.google.com/' + '/'.join(form['action'].split('/')[8:])
    new_soup = BeautifulSoup(soup.renderContents())
    for i in new_soup.findAll('a'):
        if i.has_key('href'):
            if i['href'][0:4] == 'http':
                #print i['href']
                pass
    with open(filename, 'w') as out:
        out.write(new_soup.renderContents())
        
#def replace_url(old, new):
    #for file in os.listdir('/home/josh/programming/diveintopython'):
        #if os.path.isdir(file):
            #directory = file
            #for f in os.listdir(file):
                #if 'html' in f:
                    #with open(directory + '/' + f, 'w+') as f2:
                        #text = f2.read()
                        #f2.write(re.sub('http://diveintopython.net', 'http://www.diveintopython.net', text))
if __name__ == '__main__':
    #for f in os.listdir('/home/josh/programming/diveintopython/'):
        #if ".html" in f.name:
            #purify(f)
    
    #purify('save/redhat.html')
    
    for file in os.listdir('/home/josh/programming/diveintopython'):
        if os.path.isdir(file):
            directory = file
            for f in os.listdir(file):
                if 'html' in f:
                    purify(directory + '/' + f)
                    
    #replace_url(None, None)
    
    