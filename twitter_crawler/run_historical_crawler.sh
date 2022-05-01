#!/bin/bash

# Run crawler Scenario-3 2014-2017 historical tweet from melbourne
# you can configurate it in ./config 's app_history_tweet_config.yaml

# Make sure your historical json file are located in host's /data/historical-tweets/twitter-melb.json
WORKDIR=$(cd $(dirname $0); pwd)

docker stop "historical_crawler"
docker rm "historical_crawler"

docker build -t twitter_crawler_demo:v1 .

docker run --name="historical_crawler" -e SCENARIO="3" \
 --mount type=bind,source=/data/covid-tweet-ids,target=/data/covid-tweet-ids \
 --mount type=bind,source=/data/historical-tweets/twitter-melb.json,target=/data/historical-tweets/twitter-melb.json \
 --mount type=bind,source=$WORKDIR/config,target=/twitter_crawler/config \
 twitter_crawler_demo:v1

