#!/bin/bash

#
# Given an IPv6 address scan for open ports
#

nmap -6 -n -r -v -p1-65535 -sT $1
