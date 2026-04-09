# Before Starting:

unzip the

resources folder by

right-clicking it and

hitting "extract all"

and click extract.

This should leave you

with an unzipped folder

named "resources" with

5 subdirectories.



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



# To Start Compose And Script

Inside the Sprint4Compose folder open CMD

and run: docker compose up -d --build

then once all the containers have started,

open the umami dashboard and reopen (if necessary)

CMD in the Sprint4Compose folder and run this command:

docker exec -it traffic\_generator python /app/traffic.py

continuously refresh umami to watch the views increase.

