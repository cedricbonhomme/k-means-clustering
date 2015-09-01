#! /usr/bin/python
#-*- coding:utf-8 -*

import pickle
import clusters

rownames, colnames, data = clusters.readfile("data.txt")
kclust = clusters.kcluster(data, k=10)

with open("clusters", 'wb') as f:
    pickle.dump(kclust, f)
    print("clusters stored")
