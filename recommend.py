#! /usr/bin/python
#-*- coding:utf-8 -*

# ***** BEGIN LICENSE BLOCK *****
# This file is part of Adaptive Conference Companion.
# Copyright (c) 2015 Luxembourg Institute of Science and Technology.
# All rights reserved.
#
#
#
# ***** END LICENSE BLOCK *****

__author__ = "Cedric Bonhomme"
__version__ = "$Revision: 0.2 $"
__date__ = "$Date: 2015/08/31$"
__revision__ = "$Date: 2015/10/16 $"
__copyright__ = "Copyright (c) Luxembourg Institute of Science and Technology"
__license__ = ""

import sys
import requests
import json
import pickle

import clusters
import list_clusters

def recommend(user_id, recommender_nickname, recommender_password):
    """
    Select talks/booths/poster to recommend from clusters.
    """
    recommended_talks = []
    request = requests.get(
        "https://european-data-forum.list.lu/api/v1.0/profiles.json/" + user_id,
        auth=(recommender_nickname, recommender_password))
    if request.status_code == 200:
        program = json.loads(request.text)["program"]
        progam_id = [talk["id"] for talk in program]
        with open("clusters", 'rb') as f:
            kclust = pickle.load(f)

        rownames, colnames, data = clusters.readfile("vectors.txt")

        for idx, cluster in enumerate(kclust):
            current_cluster = [rownames[r] for r in cluster]
            if set(progam_id).intersection(current_cluster):
                recommended_talks.extend(current_cluster)
    else:
        print(request.reason)

    if len(recommended_talks) != 0:
        print(recommended_talks)
        update_profile_with_recommendations(user_id, recommender_nickname,
                                                recommender_password,
                                                recommended_talks)

def update_profile_with_recommendations(user_id, recommender_nickname,
                                        recommender_password,
                                        recommended_talks):
    """
    Update the profile of the user with the previously calculated
    recommendations.
    """
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    data = []
    for talk_id in recommended_talks:
        data.append({"id":talk_id})
    payload = {"op":"add", "path":"/recommended_talks", "value":data}
    r = requests.patch(
        "https://european-data-forum.list.lu/api/v1.0/profiles.json/" + user_id,
        auth=(recommender_nickname, recommender_password),
        headers=headers, data=json.dumps(payload))
    if r.status_code == 201:
        print("Profile updated.")
    else:
        print r.reason
        print r.text


if __name__ == "__main__":
    # Point of entry in execution mode
    user_id = sys.argv[1]
    recommender_nickname = sys.argv[2]
    recommender_password = sys.argv[3]
    recommend(user_id, recommender_nickname, recommender_password)
