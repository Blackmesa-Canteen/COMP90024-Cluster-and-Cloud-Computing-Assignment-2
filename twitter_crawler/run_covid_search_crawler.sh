#!/bin/bash

# Run crawler Scenario-2 2020-07 to 2020-09 covid related tweets from melbourne
# you can configurate it in ./config 's app_covid_search_config.yaml
# to modify search range, change code in main_app.py

# Make sure your covid_related_tweet_id folder is located in host's /data/covid-tweet-ids
WORKDIR=$(cd $(dirname $0); pwd)

docker build -t twitter_crawler_demo:v1 .

docker run --name="search_crawler" -e SCENARIO="2" \
 --mount type=bind,source=/data/covid-tweet-ids,target=/data/covid-tweet-ids \
 --mount type=bind,source=/data/historical-tweets/twitter-melb.json,target=/data/historical-tweets/twitter-melb.json \
 --mount type=bind,source=$WORKDIR/config,target=/twitter_crawler/config \
 twitter_crawler_demo:v1

