Web
===

# Presentation

A recommender using K-Means clustering with the distance of Pearson.

# Usage

## Generation of the vectors

    $ ./generate_vectors.py --help
    Usage: generate_vectors.py nickname password [service_url]
    $ ./generate_vectors.py recommender passwordOfTheRecommender
    vectors saved

*generate_vectors.py* retrieves informations about talks through the API in order
to generate vectors based on different properties of a talk (abstract, resume
and title). The vectors will be stored in a simple text file.

The first argument is the nickname of the recommender. The second argument is
the password. Only use a user with the *recommender* role!

## Generation of the clusters

    $ ./generate_clusters.py --help
    Usage: generate_clusters.py nb_cluster
    $ ./generate_clusters.py 4
    Iteration 0
    Iteration 1
    clusters saved

*generate_clusters.py* launches the clustering process. Clusters are set of id
of talks or stands.

## List the generated clusters

    $ ./list_clusters.py
    Cluster 0:
    ['55e450a0c20c4956ee6f2c49', '55e450a0c20c4956ee6f2c4c', '55e450a0c20c4956ee6f2c4a']
    Cluster 1:
    ['55e450a0c20c4956ee6f2c47', '55e450a0c20c4956ee6f2c45', '55e450a0c20c4956ee6f2c4d']
    Cluster 2:
    ['55e450a0c20c4956ee6f2c48', '55e450a0c20c4956ee6f2c4b']
    Cluster 3:
    ['55e450a0c20c4956ee6f2c46']

## Recommend some talks for a user

    $ ./recommend.py 55f6791ac20c4930e106f2f6 nickname password [service_url]
    ['55f67917c20c4930de8655ff', '55f67916c20c4930de8655ea', '55f67917c20c4930de865601']

The user has previously added  the talk *55f67916c20c4930de8655ea* in its
program. Based on the clustering done previously we recommend to this
attendee 2 other talks.

# TODO

* store the final result to the server side;
* add a client for ZeroMQ;
* make it also work with cron;


# License

This code is using samples from the book
[Programming Collective Intelligence](https://www.librarything.com/work/3151375)
under MIT license.

# Contact

[Luxembourg Institute of Science and Technology](http://www.list.lu).
