#! /usr/bin/python
#-*- coding:utf-8 -*

import clusters

rownames, colnames, data = clusters.readfile("data.txt")
kclust = clusters.kcluster(data, k=10)

for cluster in kclust:
    print([rownames[r] for r in cluster])
