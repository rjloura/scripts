#!/bin/bash

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
