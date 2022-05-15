# COMP90024-Cluster-and-Cloud-Computing-Assignment-2
 Cluster & Cloud Computing, Twitter analyzer.
 
# Description
The focus of this project is toharvest tweets from Melbourne on the MRC and undertake a variety of social media data analytics
scenarios that explore liveability of Melbourne and importantly how the Twitter data can be used
alongside/compared with/augment the data available within the AURIN platform to improve our
knowledge of the liveability of Melbourne

This project is a Cloud-based solution that exploits a multitude of virtual machines (VMs)
across the MRC for harvesting tweets through the Twitter APIs (using both the Streaming and the
Search API interfaces).

We have produce a solution that can be run (in principle) across any node of the MRC to 
harvest and store tweets and scale up/down as required. The solution includes multiple
Twitter harvesting applications for Melbourne, These harvesting application running on 
the MRC together with an associated CouchDB database containing the amalgamated collection 
of Tweets. The CouchDB setup is based on a cluster setup.
