from lxml import html
from emailer import *
import requests
import json
from datetime import datetime



def check_cals(send_from, send_pass, send_to, smtp_server, name, url):
        year = datetime.now().year
	url_base = url + str(year) + '/'
	found = False

	f = open("oldagendas", "a+")
	contents = f.read()

	e = open("emails", "r")
	emails = e.readlines()

	page = requests.get(url_base)
	tree = html.fromstring(page.text)

	for l in tree.findall(".//a"):
		link = l.get("href")
                if link.startswith("/" + name + "/agendas/"):
                    continue

	        if link not in contents:
			found = True
                        print "found " + url_base + link
			for addr in emails:
				send_mail(send_from, send_pass, addr.strip(),
				    "New " + name + " Schoolboard Agenda Posted",
				    url_base + link, server=smtp_server)
			f.write(link)
	
	if not found:
		send_mail(send_from, send_pass, send_to,
		    "No new " + name + " schoolboard agendas posted", "<eom>", server=smtp_server)
	f.close()
	e.close()

with open('myenv.json', 'r') as f_env:
    d = json.load(f_env)
f_env.close()

for entry in d['agendas']:
    name = entry.keys()[0]
    url = entry[name]['url']
    check_cals(d['send_from'], d['send_pass'], d['send_to'], d['server'], name, url)
