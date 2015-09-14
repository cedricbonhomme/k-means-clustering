#! /usr/bin/python
#-*- coding:utf-8 -*

import sys
import requests
import json
import pickle

import clusters
import list_clusters


TALKS_TO_RECOMMENDED = []


def recommend(user_id):
    """
    """
    request = requests.get(
        "https://european-data-forum.list.lu/api/v1.0/profiles.json/" + user_id
        , auth=("john", "doe"))
    if request.status_code == 200:
        program = json.loads(request.text)["program"]

        with open("clusters", 'rb') as f:
            kclust = pickle.load(f)

        rownames, colnames, data = clusters.readfile("data.txt")

        for idx, cluster in enumerate(kclust):
            current_cluster = [rownames[r] for r in cluster]
            if set(program).intersection(current_cluster):
                TALKS_TO_RECOMMENDED.extend(current_cluster)

    print(TALKS_TO_RECOMMENDED)

if __name__ == "__main__":
    # Point of entry in execution mode
    user_id = sys.argv[1]
    recommend(user_id)
