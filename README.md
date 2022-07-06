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

## Usage
```
./main.py
```
