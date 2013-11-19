#!/bin/bash

#
# A simple script to toggle the proxy setting on and off in opensuse
# Proxy will already have to be configured in $PROXY_FILE and this must be
# run as root.  You may need to logout or reboot for this to take affect on
# your specific application.  But it is perfect for me when I am behind a 
# firewall, and need a proxy for yast, which does not require a
# restart|logout.
#
# If you like it, take it.  If not send it back for a full refund.
#
# rjloura@gmail.com
#

PROXY_FILE="/etc/sysconfig/proxy"
ENABLED="PROXY_ENABLED=\"yes\""
DISABLED="PROXY_ENABLED=\"no\""

if [ `grep $ENABLED $PROXY_FILE | wc -l` -eq 1 ]; then
	sed -i s/$ENABLED/$DISABLED/ $PROXY_FILE
	if [ $? -ne 0 ]; then
		echo "Error Disabling";
		exit 1;
	fi
	echo "Proxy disabled";
	exit 0;
elif [ `grep $DISABLED $PROXY_FILE | wc -l` -eq 1 ]; then
	sed -i s/$DISABLED/$ENABLED/ $PROXY_FILE
	if [ $? -ne 0 ]; then
		echo "Error Enabling";
		exit 1;
	fi
	echo "Proxy Enabled";
	exit 0;
else
	echo "Error";
	exit 1;	
fi
