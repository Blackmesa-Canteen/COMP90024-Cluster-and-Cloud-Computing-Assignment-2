# RESTful backend: python + flask

## How to use (local for now)

### Step 1

#### Install required dependencies (for now)

```bash
    pip install CouchDB
    pip install Flask
    pip install PyYAML
```

### Step 2

#### Start Flask Server (local test for now)
```bash
    cd ./backend
    python3 app.py
```

## API URL (local for now)

#### Only GET methods are allowed (for now?)

```
    http://localhost:5000/api/data-source/data-type/<sub-data-type>/<selected-view>
```

1. data-source: data source from couchDB, ["aurin", "twitter"]

2. data-type: data type from couchDB, 
  ~~`covid` `house-price` for twitter data~~ not available
    * `rai` `income` `house-price` for aurin data

3. sub-data-type: sub data type from couchDB, now only available for `house-price`
    * `rent` `sale`

4. selected-view (optional): map-reduce view, go to `util/constants.py` to see more
    * `year` `position` `type` or combination like `year-postion`