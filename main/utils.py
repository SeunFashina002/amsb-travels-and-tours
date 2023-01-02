from lib2to3.pytree import convert
import os 
from django.template.loader import render_to_string

import smtplib

import pdfkit

from pdfkit.api import configuration

from email.message import EmailMessage

EMAIL_ADDRESS = "fashinaoluwaseun36@gmail.com"
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

def send_now(client_name, image_url):
    msg = EmailMessage()
    msg['Subject'] = 'AMSB TERMS & CONDITIONS'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = ['contact.seunfashina@gmail.com', 'akoredebakare4u@gmail.com']
    msg.set_content('Hello, thanks for agreeing to our terms. Below is a copy of your agreement form. Have a nice day!')

    
    wkhtml_path = pdfkit.configuration(wkhtmltopdf = "C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")  #by using configuration you can add path value.

    rendered = render_to_string("emails/agreement.html", context={
        "client_name" : client_name,
        "image_url" : image_url
    })


    pdfkit.from_string(rendered, 'pdf/agreement.pdf', configuration = wkhtml_path)  
    result = ['pdf/output.pdf']
    for file in result:
        with open(file, 'rb') as f:
            file_data = f.read()
            file_name = f.name
            

    msg.add_attachment(file_data, maintype='application', subtype='octet-stream' ,filename=file_name)


    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        smtp.send_message(msg)


def send_apply_form(payload):
    msg = EmailMessage()
    msg['Subject'] = 'AMSB APPLICATION'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = ['contact.seunfashina@gmail.com']
    msg.set_content('Hello, here is a copy of our application form')

    
    wkhtml_path = pdfkit.configuration(wkhtmltopdf = "C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")  #by using configuration you can add path value.
    print(payload.get('first_name'))
    
    rendered = render_to_string("emails/apply.html", context={
        "first_name" : payload.get('first_name'),
        "last_name" : payload.get('last_name'),
    })


    pdfkit.from_string(rendered, 'pdf/application.pdf', configuration = wkhtml_path)  
    result = ['pdf/application.pdf']
    for file in result:
        with open(file, 'rb') as f:
            file_data = f.read()
            file_name = f.name
            

    msg.add_attachment(file_data, maintype='application', subtype='octet-stream' ,filename=file_name)


    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        smtp.send_message(msg)


