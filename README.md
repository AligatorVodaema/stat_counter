# REST API service for statistic counting.
## Service have 3 api methods:
- creating statistic.
- viewing statistics by date range.
- clearing all statistics.

### Requirements: Python3.9, Django, DRF.

## Installation with docker:
1. $ cd statistic_project/
2. $ docker-compose build
3. $ docker-compose up

## Installation:
1. create venv, activate.
2. `$ cd statistic_project/`
3. `$ pip install -r requirements.txt`
4. uncomment varible 'DATABASES' default sqlite DB in statistic_project/statistic_project/settings.py and
remove/comment varible 'DATABASES' with postgresql.
5. ` $ ./manage.py migrate `

Run: ` $ ./manage.py runserver 0.0.0.0:8000 `

### Tests:
For docker: $ docker exec -it stat_app python ./manage.py test
For local: $ ./manage.py test

## Usage:

Request body always json.

### For create statistic:
#### Request with method: POST /api/v1/create/.

 `{
    "date": "1234-3-11",
    "views": 333,
    "clicks": 22,
    "cost": "11.99"
} `

Fields: "date" is required other optional.

Returns: created instance of statistic

### For view statistic on date range:

#### Request with method: POST /api/v1/view_stat/

Date format: YYYY-MM-DD

`{
    "date_from": "0001-1-1",
    "date_to": "6666-12-12"
}`

Returns: all statistics for this date range.

Filtering:
For ordering on any field. Add query params:

` /api/v1/view_stat/?ordering=cpm `

Reverse ordering for any field:

` /api/v1/view_stat/?ordering=-views `

Default ordering: on "date" field.

### For delete all statistics:

#### Request with method: ` DELETE /api/v1/del_all_stat/ `

Returns: how much instances was deleted.



