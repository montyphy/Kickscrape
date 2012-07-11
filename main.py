#!/usr/bin/env python

from datetime import datetime

from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup


def get_content(url):
    try:
        data = urlopen(url, timeout=5).read()
    except:
        print "Cannot open url: " + url
        return None
    return data

def get_backers(soup):
    backers = soup.find('div', attrs = { 'id': 'backers_count' }).text
    backers = backers.replace(',','')
    return backers

def get_pledged(soup):
    pledged = soup.find('div', attrs = { 'id': 'pledged' }).text
    pledged = pledged.replace(',','').replace('$','')
    return pledged

def save(file_path, data):
    with open(file_path, 'a') as f:
        f.write(data)

def scrape(url, file_path='stats.txt'):
    data = get_content(url)
    if data:
        soup = BeautifulSoup(data, convertEntities=BeautifulSoup.HTML_ENTITIES)

        timestamp = datetime.now().isoformat()
        backers = get_backers(soup)
        pledged = get_pledged(soup)

        output = '{0}, {1}, {2}\n'.format(timestamp, backers, pledged)
        save(file_path, output)



if __name__=="__main__":
    url = "http://www.kickstarter.com/projects/ouya/ouya-a-new-kind-of-video-game-console"
    path = "[PATH]/stats.txt"
    scrape(url, path)