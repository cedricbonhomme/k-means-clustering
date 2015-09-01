#! /usr/bin/python
#-*- coding:utf-8 -*

import sys
import pickle

import clusters

def create_clusters(k=10):
    rownames, colnames, data = clusters.readfile("data.txt")
    kclust = clusters.kcluster(rows=data, k=k)

    with open("clusters", 'wb') as f:
        pickle.dump(kclust, f)
        print("clusters stored")

def usage(code=1):
    print("Usage: generate_clusters.py nb_cluster")
    return code

if __name__ == "__main__":
    # Point of entry in execution mode
    k = 10
    try:
        if sys.argv[1] == "--help":
            sys.exit(usage(0))
        k = int(sys.argv[1])
    except Exception as e:
        pass
    create_clusters(k)
