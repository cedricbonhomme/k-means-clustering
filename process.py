#! /usr/bin/python
#-*- coding:utf-8 -*

import clusters

rownames,colnames,data = clusters.readfile("data.txt")
kclust = clusters.kcluster(data, k=10)
print(kclust)
