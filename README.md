REST API service for statistic counting.
Service have 3 api methods:
- creating statistic.
- viewing statistics by date range.
- clearing all statistics.

Requirements: Python3.9

Installation with docker:
1. $ cd statistic_project/
2. $ docker-compose build
3. $ docker-compose up

Installation:
1. create venv, activate.
2. $ cd statistic_project/
3. $ pip install -r requirements.txt
4. uncomment default sqlite DB in statistic_project/statistic_project/settings.py and
remove postgresql.
5. $ ./manage.py migrate

Run: $ ./manage.py runserver 0.0.0.0:8000

Tests:
For docker: $ docker exec -it stat_app python ./manage.py test
For local: $ ./manage.py test

Usage:
For create statistic:
POST /api/v1/create/
{
    "date": "1234-3-11",
    "views": 333,
    "clicks": 22,
    "cost": "11.99"
}
"date" is required other optional
Filtering:
...

