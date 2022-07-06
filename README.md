# RuuviPython
Read values from RuuviTag

## Installation
### Installing Mariadb
```
sudo apt update
sudo apt install mariadb-server
sudo mysql_secure_installation
sudo systemctl start mariadb.service
```

### Create database for Mariadb
```
sudo mysql -u root -p
CREATE DATABASE ruuvi; // Or any name you want
```

### Install requirements
```
pip3 install -r requirements.txt 
```

### Next steps
- Rename .env-example to .env
- Fill .env with correct information
```
DB_HOST=ENTER YOUR DB URL HERE
DB_NAME=DB NAME HERE WHICH YOU CREATED EARLIER
DB_USER=DB USERNAME HERE
DB_PASSWORD=DB USERNAMES PASSWORD HERE
DB_PORT=DB PORT HERE
```

## Usage
```
./main.py
./main.py 120 // time between scans
```
