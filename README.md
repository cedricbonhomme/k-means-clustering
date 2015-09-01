Web
===

# Presentation

A recommender using K-Means clustering with the distance of Pearson.

# Usage

    $ ./generate_vectors.py --help
    Usage: generate_vectors.py nickname password [service_url]
    $ ./generate_vectors.py recommender passwordOfTheRecommender
    vectors saved
    $
    $ ./generate_clusters.py --help
    Usage: generate_clusters.py nb_cluster
    $ ./generate_clusters.py 4
    Iteration 0
    Iteration 1
    clusters saved
    $ ./list_clusters.py
    Cluster 0:
    ['55e450a0c20c4956ee6f2c49', '55e450a0c20c4956ee6f2c4c', '55e450a0c20c4956ee6f2c4a']
    Cluster 1:
    ['55e450a0c20c4956ee6f2c47', '55e450a0c20c4956ee6f2c45', '55e450a0c20c4956ee6f2c4d']
    Cluster 2:
    ['55e450a0c20c4956ee6f2c48', '55e450a0c20c4956ee6f2c4b']
    Cluster 3:
    ['55e450a0c20c4956ee6f2c46']


*generate_vectors.py* retrieves informations about talks through the API in order
to generate vectors based on different properties of a talk (abstract, resume
and title). The vectors will be stored in a simple text file.

The first argument is the nickname of the recommender. The second argument is
the password. Only use a user with the *recommender* role!

*generate_clusters.py* launches the clustering process. Clusters are set of id
of talks or stands.


# TODO

* store the final result to the server side with the PATCH method;
* add a client for ZeroMQ;
* make it also work with cron;
* better separation of the clustering and vectorization phases.


# License

This code is using samples from the book
[Programming Collective Intelligence](https://www.librarything.com/work/3151375)
under MIT license.

# Contact

[Luxembourg Institute of Science and Technology](http://www.list.lu).
