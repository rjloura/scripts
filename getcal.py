from lxml import html
from emailer import *
import requests



def check_cals(send_from, send_pass, send_to):
	calurl_base = 'http://www.gencourt.state.nh.us/house/caljourns/'
	calurl_main = calurl_base + 'default.htm'
	found = False

	f = open("oldcals", "a+")
	contents = f.read()

	e = open("emails", "r")
	emails = e.readlines()

	page = requests.get(calurl_main)
	tree = html.fromstring(page.text)

	for link in tree.findall(".//a"):
		url = link.get("href")
		if url.startswith("calendars/2015/") and url not in contents:
			found = True
			for addr in emails:
				send_mail(send_from, send_pass, addr.strip(),
				    "New Calendar Posted on the Gencourt site",
				    calurl_base + url)
			f.write(url)
	
	if not found:
		send_mail(send_from, send_pass, send_to,
		    "No new calendars on genncourt site", "<eom>")
	f.close()
	e.close()
