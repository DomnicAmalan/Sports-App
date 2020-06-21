from fastapi import FastAPI, BackgroundTasks
from starlette.responses import JSONResponse
from fastapi_mail import FastMail
from fastapi import Header,File, Body,Query, UploadFile
from pydantic import BaseModel,EmailStr

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