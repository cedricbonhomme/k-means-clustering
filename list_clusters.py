#! /usr/bin/python
#-*- coding:utf-8 -*

import pickle

import clusters

with open("clusters", 'rb') as f:
    kclust = pickle.load(f)

    rownames, colnames, data = clusters.readfile("data.txt")

    for idx, cluster in enumerate(kclust):
        print("Cluster {}:".format(idx))
        print([rownames[r] for r in cluster])
