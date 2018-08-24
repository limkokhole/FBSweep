#!/usr/bin/python2

#FBSweep
#https://aedenmurray.io

#Twitter: @aedenmurray

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import FirefoxProfile
from selenium.common.exceptions import TimeoutException
import mysql.connector
from bs4 import BeautifulSoup
import sys
import time
import re
import gc
import httplib
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--fbuser", action="store", required=True, help="Facebook email/phone")
parser.add_argument("--fbpass", action="store", required=True, help="Facebook password")
parser.add_argument("--dbhost", action="store", required=True, help="MYSQL database host")
parser.add_argument("--dbuser", action="store", required=True, help="MYSQL database user")
parser.add_argument("--dbpass", action="store", required=True, help="MYSQL database password")
parser.add_argument("--dbname", action="store", required=True, help="MYSQL database name")
parser.add_argument("--headless", action="store_true", help="Run in headless mode")
try:
	args = vars(parser.parse_args())
except SystemExit:
	exit(0)

db = mysql.connector.connect(
	host		= args["dbhost"],
	user		= args["dbuser"],
	passwd		= args["dbpass"],
	database	= args["dbname"]
)
cur = db.cursor()

phone		= args["fbuser"]
password	= args["fbpass"]

fp = FirefoxProfile()
fp.set_preference("dom.webnotifications.enabled", False)
options = Options()
if args["headless"]:
	options.add_argument('-headless')

driver = Firefox(executable_path='geckodriver', firefox_options=options, firefox_profile=fp)
driver.get("https://facebook.com/login.php")

print "[+] Logging in as",phone
#Login
username_box = driver.find_element_by_name("email")
username_box.clear()
username_box.send_keys(phone)

password_box = driver.find_element_by_name("pass")
password_box.clear()
password_box.send_keys(password)
driver.find_element_by_id("loginbutton").click()

#Check for login
WebDriverWait(driver, 60).until(expected.presence_of_element_located((By.CLASS_NAME, "_2s25")))
print "[+] Logged in!"

#Get to profile
soup = BeautifulSoup(driver.page_source, "lxml")
for links in soup.findAll('a', {"title":"Profile"}):
	driver.get(links.get("href"))

#Check & scan
WebDriverWait(driver, 60).until(expected.presence_of_element_located((By.CLASS_NAME, "_6-6")))
soup = BeautifulSoup(driver.page_source, "lxml")
for friends in soup.findAll('span', {"class":"_gs6"}):
	num = friends.string
	num = int(re.sub('[^0-9]', '', num))
for links in soup.findAll('a', {"data-tab-key":"friends"}):
	driver.get(links.get("href"))

print "[+] Scrolling..."
WebDriverWait(driver, 60).until(expected.presence_of_element_located((By.CLASS_NAME, "_3i9")))
for x in range(num/20):
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	time.sleep(3) # Fuck Facebook

friends_list = []
soup = BeautifulSoup(driver.page_source, "lxml")
for links in soup.findAll('a', {"class":"_5q6s"}):
	friends_list.append(links.get("href"))
print "[+] Scanning",len(friends_list),"friends..."


for link in friends_list:
	sql = "select name from people where fb_link = %s"
	cur.execute(sql, (link,))
	check = cur.fetchone()
	if check is not None:
		print "[*] " + check[0] + " already in database. Skipping..."
		continue

	time.sleep(10)
	number = "x"
	name = "x"

	try:
		driver.get(link)
		try:
			WebDriverWait(driver, 60).until(expected.presence_of_element_located((By.CLASS_NAME, "_6-6")))
		except TimeoutException as e:
			print "[!] Caught TimeoutException, skipping..."
			continue

		soup = BeautifulSoup(driver.page_source, "lxml")
		name = soup.find('a', {"class":"_2nlw _2nlv"}).text
		driver.get(soup.find("a", {"data-tab-key":"about"}).get("href"))
		try:
			WebDriverWait(driver, 60).until(expected.presence_of_element_located((By.CLASS_NAME, "_c24")))
		except TimeoutException as e:
			print "[!] Caught TimeoutException, skipping..."
			continue

		soup = BeautifulSoup(driver.page_source, "lxml")
		for text in soup.findAll("span", {"dir":"ltr"}):
			number = text.string
			number = re.sub('[^0-9]', '', number)

		#Have name number and link

		if (number != "x"):
			sql = "INSERT INTO people (name, fb_link, phonenumber) VALUES (%s, %s, %s)"
			val = (name, link, number)
			cur.execute(sql, val)
			db.commit()
		else:
			sql = "INSERT INTO people (name, fb_link) VALUES (%s, %s)"
			val = (name, link)
			cur.execute(sql, val)
			db.commit()
		print "[>] " + name + ":" + number
		soup = None
		name = None
		number = None
		val = None
		gc.collect()
	except httplib.BadStatusLine as e:
		pass
driver.close()
