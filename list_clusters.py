#! /usr/bin/python
#-*- coding:utf-8 -*

__author__ = "Cedric Bonhomme"
__version__ = "$Revision: 0.1 $"
__date__ = "$Date: 2015/08/31$"
__revision__ = "$Date: 2015/08/31 $"
__copyright__ = ""
__license__ = ""

import pickle

import clusters

def list_clusters():
    with open("clusters", 'rb') as f:
        kclust = pickle.load(f)

        rownames, colnames, data = clusters.readfile("vectors.txt")

        for idx, cluster in enumerate(kclust):
            print("Cluster {}:".format(idx))
            print([rownames[r] for r in cluster])

if __name__ == "__main__":
    # Point of entry in execution mode
    list_clusters()
