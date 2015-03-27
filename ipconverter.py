#!/usr/bin/python
import socket, struct, sys, getopt

def main(argv):
        try:
                opts, args = getopt.getopt(argv, "x")
        except getopt.GetoptError:
                print 'ipconverter.py [-x] <ipaddress as number>'
                sys.exit(1)

	if (len(args) == 0):
                print 'ipconverter.py [-x] <ipaddress as number>'
                sys.exit(1)

        if (len(opts) > 0):
		ip = int(args[0], 16)
	else:
		ip = (int)(args[0])

	"""
	Convert an IP string to long
	"""
	print socket.inet_ntoa(struct.pack('<L', ip))

if __name__ == "__main__":
    main(sys.argv[1:])

