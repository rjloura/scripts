#
# A quick email address verifier.  Not all SMTP servers will support VRFY.  If
# not then give this a shot.  Not always 100%, but seems to work with gmail,
# and a few other domains.
#

from dns.resolver import query
import smtplib
import sys


def get_mx(domain):
    '''
    These can be iterated over,  but we only need one, so just grab the first.
    for mx in query(domain, 'MX'):
        break;
    '''
    mx = query(domain, 'MX')
    mx = mx.rrset.items[0]

    # The record comes in the form '40 aspmx2.googlemail.com.'
    mx = mx.to_text().split(' ')[1]
    if mx[-1] == '.':
        mx = mx[:-1]

    return mx


test_address = sys.argv[1]
smtp_server = get_mx(test_address.split('@')[1])

smtp = smtplib.SMTP(smtp_server)

vrfy = smtp.vrfy(test_address)
if vrfy[0] != 250:
    print("Failed VRFY with ({}), but lets try RCPT.\n".format(vrfy))
else:
    print("Valid Email Address!")
    exit(0)
    

if smtp.helo("justvisiting")[0] != 250:
    print("HELO error")
    exit(1)

if smtp.mail("test@gmail.com")[0] != 250:
    print("mail from error")
    exit(1)

if smtp.rcpt(test_address)[0] != 250:
    print("Failed RCPT Invalid Email Address")
else:
    print("Valid Email Address!")

