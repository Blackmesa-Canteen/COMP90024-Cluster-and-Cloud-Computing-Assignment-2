# RESTful backend: python + flask

## How to use (local for now)

### Step 1

#### Install required dependencies (for now)

```bash
    pip install -r requirements.txt
```

### Step 2

#### Start Flask Server (local test for now)
```bash
    cd ./backend
    python3 app.py
```
#### Or you can use docker scripts to start (make sure you have docker installed)
```bash
    cd ./backend
    sh ./docker-run.sh
```

## API URL (local for now)

#### Only GET methods are allowed (for now?)

```
    http://localhost:5000/api/api-type/data-type/<sub-data-type>/<selected-view>
```

1. **api-source**: which type of api to use, ["aurin", "twitter", "scenario"]
`scenario` is for displaying some special processed data

2. **data-type**: data type from couchDB, 
    * `covid` `house-price` for twitter data
    * `rai` `income` `house-price` `migration` for aurin data

3. **sub-data-type**: sub data type from couchDB, now only available for `house-price`
    * `rent` `sale`

4. **selected-view** (optional): map-reduce view, go to `util/constants.py` to see more
    * `year` `position` `type` or combination like `year-postion`
    * `sex` `English` or `english` for migration data
    * `subjectivity` `polarity` `language` for twitter data

## API URL From

<table>
    <tr> 
    	<th rowspan="1">api-type</th>
        <th rowspan="1">data-type</th>
        <th rowspan="1">sub-data-type</th>
        <th rowspan="1">selected-view</th>
   </tr>
   <tr> 
		<td rowspan="14">aurin</td>
   		<td rowspan="3">income</td>
   		<td rowspan="3">none</td>
   		<td>year</td>
   </tr>
   <tr> 
   		<td>position</td>
   </tr>
   <tr> 
   		<td>2-combination (eg: year-position)</td>
   </tr>
   <tr> 
        <td rowspan="5">house-price</td>
        <td rowspan="5">rent or sale</td>
   		<td>position</td>
   </tr>
   <tr> 
   		<td>year</td>
   </tr>
   <tr> 
   		<td>type</td>
   </tr>
   <tr> 
   		<td>2-combination (eg: year-position)</td>
   </tr>
   <tr> 
   		<td>sumary</td>
   </tr>
   <tr> 
        <td rowspan="5">migration</td>
        <td rowspan="5">none</td>
   		<td>sex</td>
   </tr>
   <tr> 
   		<td>year</td>
   </tr>
   <tr> 
   		<td>population</td>
   </tr>
   <tr> 
   		<td>total-population</td>
   </tr>
   <tr> 
   		<td>english or English</td>
   </tr>
   <tr> 
        <td>rai</td>
        <td>none</td>
   		<td>none</td>
   </tr>
   <tr> 
		<td rowspan="11">twitter</td>
   		<td rowspan="7">house-price</td>
   		<td rowspan="7">none</td>
   		<td>year</td>
   </tr>
   <tr> 
   		<td>polarity</td>
   </tr>
   <tr> 
   		<td>subjectivity</td>
   </tr>
   <tr> 
   		<td>map</td>
   </tr>
   <tr> 
   		<td>language</td>
   </tr>
   <tr> 
   		<td>language-time (time: [month, quarter, year])</td>
   </tr>
   <tr> 
   		<td>map-year</td>
   </tr>
    <tr> 
        <td rowspan="4">covid</td>
        <td rowspan="4">none</td>
   		<td>polarity</td>
   </tr>
   <tr> 
   		<td>subjectivity</td>
   </tr>
   <tr> 
   		<td>language</td>
   </tr>
   <tr> 
   		<td>language-time (time: [month, quarter, year])</td>
   </tr>
   <tr> 
		<td rowspan="2">scenario</td>
   		<td>languages</td>
   		<td>none</td>
   		<td>none</td>
   </tr>
   <tr> 
   		<td>languages-month</td>
        <td>none</td>
   		<td>none</td>
   </tr>
</table>

