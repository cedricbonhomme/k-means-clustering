#! /usr/bin/python
#-*- coding:utf-8 -*

__author__ = "Cedric Bonhomme"
__version__ = "$Revision: 0.3 $"
__date__ = "$Date: 2015/08/31$"
__revision__ = "$Date: 2015/10/26 $"
__copyright__ = ""
__license__ = ""

import sys
import requests
import json
import pickle

import clusters
import list_clusters

def recommend(user_id, recommender_nickname, recommender_password,
                service_url):
    """
    Select talks/booths/poster to recommend from clusters.
    """
    recommended_talks = []
    request = requests.get(service_url + "/api/v1.0/profiles.json/" + user_id,
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

    return recommended_talks

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
    r = requests.patch(service_url + "/api/v1.0/profiles.json/" + user_id,
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
    try:
        service_url = sys.argv[4]
    except Exception as e:
        service_url = ""

    recommended_talks = recommend(user_id, recommender_nickname,
                                    recommender_password, service_url)

    if len(recommended_talks) != 0:
        print("Talks to recommend:")
        print(recommended_talks)
        print("Updating profile...")
        update_profile_with_recommendations(user_id, recommender_nickname,
                                                recommender_password,
                                                recommended_talks)
    else:
        print("Nothing to recommend.")
