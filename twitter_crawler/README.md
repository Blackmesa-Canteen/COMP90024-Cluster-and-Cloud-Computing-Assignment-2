# Introduction

Crawl tweets via Twitter api V2， parse and put them in CouchDB.

There are 3 scenarios of twitter crawlers:
- Stream crawler that continues fetching latest tweets in melbourne, can search by keywords.
- Search crawler for COVID related tweets in melbourne, the search IDs is provided by local file. The time period is within 2020.
- History Tweets JSON file crawler that reads tweets from local file provided by the subject, can search by keywords. The time period is 2014-07 to 2017-6

# Usage

## 0. Install Dependencies
```bash
pip install -r requirements.txt
```

## 1. Configuration file

There are 4 configuration files in `/config` directory. You can edit configuration here.


## 2. Prepare data file
If the scenario you use that needs local file(such as `historical-tweet-file`or `covid-tweet-id-file`), please put them in some directory, and set up their paths in the configuration file.

## 3. Run

Run the main_app.py script with `-s` argument to declare which scenario to run.

```bash
python3 main_app.py -s 1 # run the first Scenario
```


# Reference

We used `COVID-19-TweetIDs` open source project's historical tweet IDs about COVID-19.

This dataset is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International Public License (CC BY-NC-SA 4.0).

Chen E, Lerman K, Ferrara E Tracking Social Media Discourse About the COVID-19 Pandemic: Development of a Public Coronavirus Twitter Data Set JMIR Public Health Surveillance 2020;6(2):e19273 DOI: 10.2196/19273 PMID: 32427106