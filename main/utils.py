import os 
import smtplib
from email.message import EmailMessage
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
# from amsb.settings import EMAIL_ADDRESS, EMAIL_PASSWORD

class Render:

    @staticmethod
    def render(path: str, params: dict):
        template = get_template(path)
        html = template.render(params)
        response = BytesIO()
        file = open("myfile.pdf", "wb")
        pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), file)
        file.close()
        if not pdf.err:
            return HttpResponse(response.getvalue(), content_type='application/pdf')
        else:
            return HttpResponse("Error Rendering PDF", status=400)

    @staticmethod
    def render_to_file(path: str, params: dict):
        template = get_template(path)
        html = template.render(params)
        extract_file = f"{path.split('/')[1]}"
        file_name = f"{extract_file.split('.')[0]}"
        file_path = f"pdf/{file_name}.pdf"
        with open(file_path, 'wb') as pdf:
            pisa.pisaDocument(BytesIO(html.encode("UTF-8")), pdf)
        return [file_name, file_path]

EMAIL_ADDRESS='mailbot.amsbconnectsltd@gmail.com'
EMAIL_PASSWORD='UOZgDyTuzbO9saLBoZxX'


def send_now(client_name, image_url, user_email):
    msg = EmailMessage()
    msg['Subject'] = 'AMSB TERMS & CONDITIONS'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = [user_email, 'amsbconnectsltd@outlook.com']
    msg.set_content('Hello, thanks for agreeing to our terms. Below is a copy of your agreement form. Have a nice day!')

    data = {
    "client_name" : client_name,
    "image_url" : image_url,
	}


    pdf = Render.render_to_file('emails/agreement.html', data)
    
    with open(pdf[1], 'rb') as f:
        file_data = f.read()
        file_name = f"{pdf[1].split('/')[1]}"
        
    
    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)


    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        smtp.send_message(msg)


def send_apply_form(payload, user_email):
    msg = EmailMessage()
    msg['Subject'] = 'AMSB APPLICATION'
    msg['From'] = EMAIL_ADDRESS
    
    msg['To'] = [user_email, 'amsbconnectsltd@outlook.com']
    print(user_email)
    msg.set_content('Hello, here is a copy of your application form')

    data = {
        "first_name" : payload.get('first_name'),
        "middle_name" : payload.get('middle_name'),
        "last_name" : payload.get('last_name'),
        "dob" : payload.get('dob'),
        "gender" : payload.get('gender'),
        "relationship" : payload.get('relationship'),
        "employment" : payload.get('employment'),
        "adress" : payload.get('adress'),
        "citizenship" : payload.get('citizenship'),
        "email" : payload.get('email'),
        "tel" : payload.get('tel'),
        "high_school" : payload.get('high_school'),
        "post_secondary_sch" : payload.get('post_secondary_sch'),
        "work" : payload.get('work'),
        "travel" : payload.get('travel'),
        "travel_place" : payload.get('travel_place'),
        "illness" : payload.get('illness'),
        "accomodation" : payload.get('accomodation'),
        "native_lang" : payload.get('native_lang'),
        "other_lang" : payload.get('other_lang'),
        "passport_num" : payload.get('passport_num'),
        "issue_date_passport" : payload.get('issue_date_passport'),
        "expire_date_passport" : payload.get('expire_date_passport'),
        "visa_refusal" : payload.get('visa_refusal'),
        "visa_refusal_reason" : payload.get('visa_refusal_reason'),
	}

    print('data', data)
    pdf = Render.render_to_file('emails/apply.html', data)
    
    with open(pdf[1], 'rb') as f:
        file_data = f.read()
        file_name = f"{pdf[1].split('/')[1]}"
        
    
    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        smtp.send_message(msg)
