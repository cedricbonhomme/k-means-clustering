#! /usr/bin/python
#-*- coding:utf-8 -*

import sys
import re
import requests
import json

# load the stopwords
data=None
with open("stopwords.txt", 'r') as f:
    data = f.read()
STOP_WORDS = data.split(";")


def getwords(text):
    # Split words by all non-alpha characters
    words = re.compile(r'[^A-Z^a-z]+').split(text)

    # Convert to lowercase
    return [word.lower() for word in words if word!='']

def remove_stopwords(words):
    """
    Remove the stop words from a list of words.
    """
    return [w for w in words if w not in STOP_WORDS]

def get_word_counts(talk):
    # Parse the feed
    wc = {}
    # Extract a list of words
    words = getwords(talk["title"] + talk["resume"] + ' ' + talk["abstract"])
    words = remove_stopwords(words)
    for word in words:
        wc.setdefault(word, 0)
        wc[word] += 1
    return talk["id"] , wc

def retrieve_data(url, nickname, password):
    r = requests.get(url, auth=(nickname, password))
    if r.status_code != 200:
        print("Problem when connecting to {}: {}".format(url, r.reason))
        sys.exit(1)
    talks = json.loads(r.text)
    return talks

def generate_vectors(url, nickname, password):
    talks = retrieve_data(url, nickname, password)

    apcount={}
    wordcounts={}
    for talk in talks:
        talk_id, wc = get_word_counts(talk)
        wordcounts[talk_id] = wc
        for word, count in wc.items():
          apcount.setdefault(word,0)
          if count>1:
            apcount[word]+=1

    wordlist=[]
    for w,bc in apcount.items():
        frac = float(bc)/len(talks)
        if frac>0.1 and frac<0.5:
            wordlist.append(w)

    out = open('data.txt','w')
    out.write('id')
    for word in wordlist:
        out.write('\t%s' % word)
    out.write('\n')
    for talk_id, wc in wordcounts.items():
        out.write(talk_id)
        for word in wordlist:
            if word in wc:
                out.write('\t%d' % wc[word])
            else:
                out.write('\t0')
        out.write('\n')
    print("vectors saved")

def usage(code=1):
    """
    Display usage information.
    """
    print("Usage: generate_vectors.py nickname password [service_url]")
    return code

if __name__ == "__main__":
    # Point of entry in execution mode
    try:
        if sys.argv[1] == "--help":
            sys.exit(usage(0))
        nickname, password = sys.argv[1], sys.argv[2]
    except Exception as e:
        sys.exit(usage())
    try:
        service_url = sys.argv[3]
    except:
        service_url = "http://european-data-forum.list.lu/api/v1.0/talks.json"
    generate_vectors(service_url, nickname, password)
