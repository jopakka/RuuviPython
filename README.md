# RuuviPython
Read values from RuuviTag

## Installation
### Installing Mariadb
```cmd
sudo apt update
sudo apt install mariadb-server
sudo mysql_secure_installation
sudo systemctl start mariadb.service
```

### Create database for Mariadb
```c
sudo mysql -u root -p
CREATE DATABASE ruuvi; // Or any name you want
```

### Install requirements
```cmd
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
```cmd
./main.py
./main.py 120 // time between scans
```

## Install as service
```cmd
cd /lib/systemd/system/
sudo nano ruuvi_python.service
```

Copy this to ruuvi_python.service and replace USERNAME and INSTALL_PATH with correct values and add args if you want.
```
[Unit]
Description=RuuviPython Service
After=multi-user.target

[Service]
Type=simple
User=USERNAME
ExecStart=/usr/bin/python INSTALL_PATH
Restart=on-abort

[Install]
WantedBy=multi-user.target
```

Now activate service. Replace INSTALL_PATH with correct path.
```cmd
sudo chmod 644 /lib/systemd/system/ruuvi_python.service
chmod +x INSTALL_PATH/main.py
sudo systemctl daemon-reload
sudo systemctl enable ruuvi_python.service
sudo systemctl start ruuvi_python.service
```

### Check service status
```cmd
sudo systemctl status ruuvi_python.service
```