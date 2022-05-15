# COMP90024-Cluster-and-Cloud-Computing-Assignment-2
 
## Introduction
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

## Tech stack
- Python + Flask
- Tweepy
- CouchDB
- React.js
- Docker
- Nginx

## License
```
MIT License

Copyright (c) 2022 COMP90024-2022 Group 52

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
