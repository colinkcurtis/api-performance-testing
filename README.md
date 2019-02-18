# api-performance-testing
##A set of scripts for testing APIs and other requestable services


## To use this repo:
###$brew install libev ###necessary for the locustio dependency, gevent

### $python3 -m venv YOUR_NEW_ENV
### $pip install --upgrade pip ###recommended
### $pip install locustio
### $git clone git@github.com:colinkcurtis/api-performance-testing
### $cd api-performance-testing
### A sample command to run:
### $locust -f onto_api_locust.py --host=http://localhost:5000 ###relevant if you are running an Onto API host locally
### Navigate in the browser to 0.0.0.0:8089 to run the locust utility and observe and gather outputs...