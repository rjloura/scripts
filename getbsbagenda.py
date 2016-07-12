from lxml import html
from emailer import *
import requests
import json
from datetime import datetime



def check_cals(send_from, send_pass, send_to, smtp_server):
        year = datetime.now().year
	url_base = 'http://www.sau41.org/Brookline/agendas/' + str(year) + '/'
	found = False

	f = open("oldagendas", "a+")
	contents = f.read()

	e = open("emails", "r")
	emails = e.readlines()

	page = requests.get(url_base)
	tree = html.fromstring(page.text)

	for link in tree.findall(".//a"):
		url = link.get("href")
                if url.startswith("/Brookline/agendas/"):
                    continue

	        if url not in contents:
			found = True
                        print "found " + url_base + url
			for addr in emails:
				send_mail(send_from, send_pass, addr.strip(),
				    "New Brookline Schoolboard Agenda Posted",
				    url_base + url, server=smtp_server)
			f.write(url)
	
	if not found:
		send_mail(send_from, send_pass, send_to,
		    "No new agendas posted", "<eom>", server=smtp_server)
	f.close()
	e.close()

with open('myenv.json', 'r') as f_env:
    d = json.load(f_env)
f_env.close()

check_cals(d['send_from'], d['send_pass'], d['send_to'], d['smtp_server'])
