#! /usr/bin/python
#-*- coding:utf-8 -*

import re
import requests
import json

def getwords(text):
    # Split words by all non-alpha characters
    words = re.compile(r'[^A-Z^a-z]+').split(text)

    # Convert to lowercase
    return [word.lower() for word in words if word!='']

def remove_stropwords(words):
    data=None
    with open("stopwords.txt", 'r') as f:
        data = f.read()
    stop_words = data.split(";")
    return [w for w in words if w not in stop_words]

def getwordcounts(talk):
    # Parse the feed
    wc = {}
    # Extract a list of words
    words = getwords(talk["resume"] + ' ' + talk["abstract"])
    words = remove_stropwords(words)
    for word in words:
        wc.setdefault(word, 0)
        wc[word] += 1
    return talk["id"] , wc

def generate_vectors(url, nickname, password):
    r = requests.get(url, auth=(nickname, password))
    talks = json.loads(r.text)

    apcount={}
    wordcounts={}
    for talk in talks:
        talk_id, wc = getwordcounts(talk)
        wordcounts[talk_id] = wc
        for word, count in wc.items():
          apcount.setdefault(word,0)
          if count>1:
            apcount[word]+=1

    wordlist=[]
    for w,bc in apcount.items():
      frac=float(bc)/len(talks)
      if frac>0.1 and frac<0.5:
        wordlist.append(w)

    out=open('data.txt','w')
    out.write('id')
    for word in wordlist: out.write('\t%s' % word)
    out.write('\n')
    for blog, wc in wordcounts.items():
      print(blog)
      out.write(blog)
      for word in wordlist:
        if word in wc: out.write('\t%d' % wc[word])
        else: out.write('\t0')
      out.write('\n')







if __name__ == "__main__":
    generate_vectors("http://european-data-forum.list.lu/api/v1.0/talks.json",
                        "recommender", "recommenderPassword")
