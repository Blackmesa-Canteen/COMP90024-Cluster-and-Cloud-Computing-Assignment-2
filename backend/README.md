# RESTful backend: python + flask

## How to use

### Step 1

#### Install required dependencies

```bash
    pip install -r requirements.txt
```

### Step 2

#### Start Flask Server
```bash
    cd ./backend
    python3 app.py
```
#### Or you can use docker scripts to start (make sure you have docker installed)
```bash
    cd ./backend
    sh ./docker-run.sh
```

## API URL

#### Only GET methods are allowed

```
    http://Host:Port/api/api-type/data-type/selected-view
    http://Host:Port/api/api-type/scenario-view
```

1. **api-source**: which type of api to use, ["aurin", "twitter", "scenario"]
`aurin` `twitter` is only for developing phase
`scenario` is for displaying demo data

2. **data-type**: data type from couchDB, 
    * `covid` `house-price` for twitter data
    * `income` `house-price` `migration` for aurin data

3. **selected-view**: map-reduce view, go to `util/constants.py` to see more
    * `year` `position` `type` or combination like `year-postion`
    * `sex` `English` or `english` for migration data
    * `subjectivity` `polarity` `language` for twitter data

4. **scenario-view**: finally used in the system
    * `languages` `languages-month` for scenario **Overseas Migration and Languagues Languages On Twitter**
    * `house-price` for scenario **Relevance among House price, Income and Attitudes of People On Twitter**
    * `covid` for scenario **How Decisions (Lockdown) made By Local Government Influence Employment and People's Feeling**
    * `stream` for scenario **General Statistics of Real-time Tweets, and details of these Tweets**