import smtplib
import mimetypes
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate


def send_mail(send_from, send_pass, send_to, subject, text, files=None,
              server=""):
    #assert isinstance(send_to, list)

    msg = MIMEMultipart()

    msg['Subject'] = subject
    msg['From'] = send_from
    msg['To'] = send_to
    msg['Date'] = formatdate(localtime=True)

    msg.attach(MIMEText(text))

    '''
    for f in files or []:
        with open(f, "rb") as fil:
            msg.attach(MIMEApplication(
                fil.read(),
                Content_Disposition='attachment; filename="%s"' % basename(f)
            ))
    '''

    if files:
        ctype, encoding = mimetypes.guess_type(files)
        if ctype is None or encoding is not None:
            ctype = "application/octet-stream"

        maintype, subtype = ctype.split("/", 1)

        if maintype == "text":
            fp = open(files)
            attachment = MIMEText(fp.read(), _subtype=subtype)
            fp.close()
        else:
            # TODO: implement more types
            assert 0

        attachment.add_header("Content-Disposition", "attachment", filename=files)
        msg.attach(attachment)

    smtp = smtplib.SMTP(server)
    smtp.starttls()
    smtp.login(send_from, send_pass)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()



'''
def send_mail(send_from, send_pass, send_to, subject, text, files=None,
        server="", port=587):
    msg = MIMEText(text)
    msg['Subject'] = subject
    msg['From'] = send_from
    msg['To'] = send_to

    smtp = smtplib.SMTP(server)
    smtp.starttls()
    smtp.login(send_from, send_pass)
    smtp.sendmail(send_from, [send_to], msg.as_string())
    smtp.quit()
'''

