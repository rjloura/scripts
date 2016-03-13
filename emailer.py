import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate


'''
def send_mail(send_from, send_to, subject, text, files=None,
              server=""):
    assert isinstance(send_to, list)

    msg = MIMEMultipart(
        From=send_from,
        To=COMMASPACE.join(send_to),
        Date=formatdate(localtime=True),
        Subject=subject
    )
    msg.attach(MIMEText(text))

    for f in files or []:
        with open(f, "rb") as fil:
            msg.attach(MIMEApplication(
                fil.read(),
                Content_Disposition='attachment; filename="%s"' % basename(f)
            ))

    smtp = smtplib.SMTP(server)
    smtp.login("name", "pass")
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()
'''



def send_mail(send_from, send_pass, send_to, subject, text, files=None,
        server=""):
    msg = MIMEText(text)
    msg['Subject'] = subject
    msg['From'] = send_from
    msg['To'] = send_to

    smtp = smtplib.SMTP(server)
    smtp.login(send_from, send_pass)
    smtp.sendmail(send_from, [send_to], msg.as_string())
    smtp.quit()
