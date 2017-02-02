#!/bin/bash

IFS='
'
for d in `ls -lt | grep ^d|awk '{print $9}'`; do du -h $d | tail -1; done
