#!/bin/bash

# A little script that would contain my credentials to an SMTP relay, that
# would run the getcal.py script, to email me new calendars and journals from
# the gencourt website.

cd /home/rui/scripts/gencourt;
python -c 'from getcal import check_cals; check_cals(<username@relayname.com>, <password>, <destination>)'
