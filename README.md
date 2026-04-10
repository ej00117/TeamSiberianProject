# Before Starting:

unzip the

resources folder by

right-clicking it and

hitting "extract all"

and click extract.

This should leave you

with an unzipped folder

named "resources" with

4 subdirectories.



## BookStack website

http://localhost:8080

## Umami analytics dashboard

http://localhost:3000

## BookStack Login

Email: admin@admin.com  
Password: password

## Umami Login

Email: admin  
Password: umami

TO START COMPOSE AND SCRIPT

Inside the Sprint4PatrickCompose folder open CMD
and run: docker compose up --build

Everything should start working and the traffic generator should start sending traffic.

If the traffic generator doesn't start working, run these one after the other.
1. docker compose build traffic_generator
2. docker compose up traffic_generator

Once the traffic generator is up and running, open the umami dashboard and continuously refresh umami to watch as the views increase.
