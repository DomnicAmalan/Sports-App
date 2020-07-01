from fastapi import FastAPI, BackgroundTasks
from starlette.responses import JSONResponse
from fastapi_mail import FastMail
from fastapi import Header,File, Body,Query, UploadFile
from pydantic import BaseModel,EmailStr
import socket
import smtplib
import dns.resolver

html = """
<html> 
<body>
<p>Hi This test mail
<br>Thanks for using Fastapi-mail</p> 
</body> 
</html>
"""

template = """
<html> 
<body>
<p>Hi This test mail using BackgroundTasks
<br>Thanks for using Fastapi-mail</p> 
</body> 
</html>
"""

async def send_email(email: str) -> JSONResponse:
    print(email)
    #as gmail requires TLS connection, therefore you require to set tls to True
    mail = FastMail(email="amalandomnic@gmail.com",password="xenqEf-2guvha-kadnox",tls=True,port="587",service="gmail")

    await mail.send_message(recipient=email,subject="Test email from fastapi-mail", body=html, text_format="html")

    return JSONResponse(status_code=200, content={"message": f"email has been sent {email} address"})


def check_mail(mail):
    domain = mail.split("@")[1]
    records = dns.resolver.query(domain, 'MX')
    mxRecord = records[0].exchange
    mxRecord = str(mxRecord)
    # Get local server hostname
    host = socket.gethostname()

    # SMTP lib setup (use debug level for full output)
    server = smtplib.SMTP()
    server.set_debuglevel(0)

    # SMTP Conversation
    server.connect(mxRecord)
    server.helo(host)
    server.mail('amalandomnic@gmail.com')
    code, message = server.rcpt(str(mail))
    server.quit()
    if code == 250:
        return True
    else:
        return False
