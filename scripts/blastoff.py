#!/usr/bin/python2
import mysql.connector
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--dbhost", action="store", required=True, help="MYSQL database host")
parser.add_argument("--dbuser", action="store", required=True, help="MYSQL database user")
parser.add_argument("--dbpass", action="store", required=True, help="MYSQL database password")
parser.add_argument("--dbname", action="store", required=True, help="MYSQL database name")
args = vars(parser.parse_args())

db = mysql.connector.connect(
	host		= args["dbhost"],
	user		= args["dbuser"],
	passwd		= args["dbpass"],
	database	= args["dbname"]
)

cur = db.cursor(buffered=True)
cur2 = db.cursor(buffered=True)

def handle(res):
	if(res[2] == False):
		print "[*] SMS -> " + res[1] + " : " + res[0].split(" ")[0]
		os.system("./facebook_sms.sh " + res[1] + " " + res[0].split(" ")[0] + " > /dev/null 2>&1")
		cur2.execute("update people set hit = True where phonenumber = '" + res[1] + "';")
		db.commit()
	else:
		print "[!] " + res[0] + " has already been hit. Skipping..."

cur.execute("select name, phonenumber, hit from people where phonenumber is not null;")
res = cur.fetchone()
while res:
	handle(res)
	res = cur.fetchone()
