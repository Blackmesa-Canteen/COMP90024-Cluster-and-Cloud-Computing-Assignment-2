# Run crawler Scenario-1 Stream tweets from melbourne
# you can configurate it in ./config 's app_twitter_stream_config.yaml

docker build -t twitter_crawler_demo:v1 .

docker run --name="crawler" -e SCENARIO="1" \
 --mount type=bind,source=/data/covid-tweet-ids,target=/data/covid-tweet-ids \
 --mount type=bind,source=/data/historical-tweets/twitter-melb.json,target=/data/historical-tweets/twitter-melb.json \
 --mount type=bind,source=./config,target=/twitter_crawler/config \
 twitter_crawler_demo:v1

