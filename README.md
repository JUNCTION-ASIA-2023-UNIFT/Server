# Server
Backend Server repository

## How to Run ? 

### 1️. Set .env file

|NAME|VAlUE|
|---|:---|
|MYSQL_HOST|mysql host name|
|MYSQL_DATABASE|mysql database name|
|MYSQL_USER|mysql user name|
|MYSQL_PASSWORD|mysql user password|
|MYSQL_ROOT_PASSWORD|mysqlroot password|

### 2️. Run Doker Compose
Run Container
```
docker-compose up --build -d
```

Shut down 
```
docker-compose down 

-- if you want to delete volumn
docker-compose down -v
```