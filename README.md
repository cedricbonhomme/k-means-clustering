Web
===

# Presentation

A recommender using K-Means clustering with the distance of Pearson.

# Usage

## Generation of the vectors

    $ ./generate_vectors.py --help
    Usage: generate_vectors.py [window_min] [window_max] [service_url]
    $ ./generate_vectors.py
    vectors saved

*generate_vectors.py* retrieves informations about talks through the API in order
to generate vectors based on different properties of a talk (abstract, resume
and title). The vectors will be stored in a simple text file.

The size of the window will have an impact on the size of the vectors and so
important impact on the boundaries between the clusters.

## Generation of the clusters

    $ ./generate_clusters.py --help
    Usage: generate_clusters.py nb_cluster
    $ ./generate_clusters.py 15
    Iteration 0
    Iteration 1
    Iteration 2
    Iteration 3
    clusters saved

*generate_clusters.py* launches the clustering process. Clusters are set of id
of talks or booths.

* More clusters generated means more iterations for less recommendations
and better recommendations.
* Less clusters generated means less iterations for more recommendations
and less relevant recommendations.

For more clusters and to keep a good quality we need to have more and bigger
vectors.

## List the generated clusters

    $ ./list_clusters.py
    Cluster 0:
    ['55e450a0c20c4956ee6f2c49', '55e450a0c20c4956ee6f2c4c', '55e450a0c20c4956ee6f2c4a']
    Cluster 1:
    ['55f67917c20c4930de8655ff', '55f67916c20c4930de8655ea', '55f67917c20c4930de865601']
    Cluster 2:
    ['55e450a0c20c4956ee6f2c48', '55e450a0c20c4956ee6f2c4b']
    Cluster 3:
    ['55e450a0c20c4956ee6f2c46']
    .
    .
    .
    <snip>
    .
    .
    .


## Recommend some talks for a user

    $ ./recommend.py 55f6791ac20c4930e106f2f6 recommender_nickname recommender_nickname [service_url]
    ['55f67917c20c4930de8655ff', '55f67916c20c4930de8655ea', '55f67917c20c4930de865601']
    Profile updated.

The user has previously added  the talk *55f67916c20c4930de8655ea* in its
program. Based on the clustering done previously we recommend to this
attendee 2 other talks.

The second argument is the nickname of the recommender. The third argument is
the password. Only use a user with the *recommender* role!

# TODO

* add a client for ZeroMQ;
* make it also work with cron;
* add a way to let the user choose another distance calculation than Pearson.


# License

This code is using samples from the book
[Programming Collective Intelligence](https://www.librarything.com/work/3151375)
under MIT license.

# Contact

[Luxembourg Institute of Science and Technology](http://www.list.lu).
