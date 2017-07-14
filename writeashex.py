import binascii, sys, os


def usage():
    print("\tUsage: writeashex.py <hex string> <outputfile>")
    quit(1)
    
if len(sys.argv) != 3:
    usage()

intext = sys.argv[1]
outfile = sys.argv[2]

if len(intext) % 2 != 0:
    print("\tHex string must be even length.")
    quit(1)

if os.path.isfile('./' + outfile):
    print('file "{}" exists'.format(outfile))
    quit(1)


f = open(outfile, 'wb')
outbytes = f.write(binascii.unhexlify(intext))
print("{}bytes written".format(outbytes or ''))
f.close()

