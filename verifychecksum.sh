#!/bin/bash


function fail {
	echo -e "\n\tusage: md5check.sh [hashalgo] <hash> <filename>"
	echo -e "\nSupported hash algorithms: \n" \
		"\t-md5\tMD5 checksum\n" \
		"\t-sha256\tSHA256 checksum\n" 
	exit 1
}

[[ $# -ne 3 ]] && fail;

while true; do
    case "$1" in 
        -sha256)
		CHKSUM_PROG=sha256sum
		break
		;;
	-md5)
		CHKSUM_PROG=md5sum
		break
		;;
	*)
		echo $1
		break
		fail
		;;
    esac
done

echo -e "$2 $3" | $CHKSUM_PROG -c -
