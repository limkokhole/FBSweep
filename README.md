# FBSweep
Crawls your Facebook friends list looking for phone numbers to launch phishing attacks.

#### Disclaimer: For educational purposes only

[![Build Status](https://travis-ci.org/aedenmurray/FBSweep.svg?branch=master)](https://travis-ci.org/aedenmurray/FBSweep)
![AUR](https://img.shields.io/aur/license/yaourt.svg)

## Requirements:
#### Arch Linux:
```
# pip2 install selenium
# pip2 install beautifulsoup4
# pip2 install mysql-connector-python
# pacman -S geckodrvier 
# pacman -S firefox
# pacman -S python2-lxml
```
## Initial Setup:
FBSweep reads and writes from either a local or remote MYSQL database. 

The database structure is as follows:
```
[people]
+-------------+--------------+------+-----+---------+----------------+
| Field       | Type         | Null | Key | Default | Extra          |
+-------------+--------------+------+-----+---------+----------------+
| id          | int(11)      | NO   | PRI | NULL    | auto_increment |
| name        | varchar(100) | YES  |     | NULL    |                |
| fb_link     | varchar(250) | YES  |     | NULL    |                |
| phonenumber | varchar(11)  | YES  |     | NULL    |                |
| fb_password | varchar(250) | YES  |     | NULL    |                |
| hit         | tinyint(1)   | YES  |     | 0       |                |
+-------------+--------------+------+-----+---------+----------------+
```
Once the database is setup and the variables are set then you can proceed to use the framework.
## Usage:
```
usage: fbsweep.py [-h] --fbuser FBUSER --fbpass FBPASS --dbhost DBHOST
                  --dbuser DBUSER --dbpass DBPASS --dbname DBNAME [--headless]

optional arguments:
  -h, --help       show this help message and exit
  --fbuser FBUSER  Facebook email/phone
  --fbpass FBPASS  Facebook password
  --dbhost DBHOST  MYSQL database host
  --dbuser DBUSER  MYSQL database user
  --dbpass DBPASS  MYSQL database password
  --dbname DBNAME  MYSQL database name
  --headless       Run in headless mode

```

## Setup fake site:
The 3 files you need are in the [html](html/) folder. Setup a webserver with PHP and mysqli enabled. If you setup your database like mine then the SQL queries in [succ.php](html/succ.php) should work fine. **Don't forget to replace the MYSQL datbase info in [succ.php](html/succ.php) with your information.** 


## Launching the scan:
```
./fbsweep.py <OPTIONS>
```

## Launching a phishing attack:
Once your database has been populated - you can use the [blastoff.py](blastoff.py) to scan the database and automatically run the [facebook_sms.sh](facebook_sms.sh) script. To successfully launch the attack you need to edit the [facebook_sms.sh](facebook_sms.sh) to use a SMS service provider. The one that comes bundled is using [SinchSMS](https://www.sinch.com/products/sms-api/) - you will need to sign up for an account and add credits to use it.
```
./blastoff.py
```
