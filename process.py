#! /usr/bin/python
#-*- coding:utf-8 -*

import clusters

rownames, colnames, data = clusters.readfile("data.txt")
kclust = clusters.kcluster(data, k=10)

for idx, cluster in enumerate(kclust):
    print("Cluster {}:".format(idx))
    print([rownames[r] for r in cluster])
