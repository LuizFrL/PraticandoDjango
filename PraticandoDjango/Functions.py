from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP
from django.contrib import messages
from django.contrib.auth.models import User
from PraticandoDjango.CONSTANTS import EMAIL, PASS_EMAIL
from typing import Dict, Union, Tuple


class AuthenticationValid(object):

    def __init__(self, request):
        self.request = request

    def valid_register_form(self, form: Dict[str, Union[int, str]]) -> bool:
        campos_sem_espacos: Tuple = (
            form['password1'].strip(), form['password2'].strip(),
            form['username'].strip(), form['email'].strip(),
            form['funcao'].strip(), form['name1'].strip(),
            form['name2'].strip()
        )
        if all(campos_sem_espacos):
            if form['password1'] == form['password2']:
                user = User.objects.filter(username=form['username'])
                if not user.exists():
                    return True
                messages.error(self.request, 'Username já existente, favor escolher outro.', 'danger')
                return False
            messages.error(self.request, 'Senhas devem ser iguais.', 'danger')
            return False
        messages.error(self.request, 'Campos não podem conter apenas espaços.', 'danger')
        return False


class SendEmail(object):
    def __init__(self, request):
        self.request = request
        self.email = EMAIL
        self.senha = PASS_EMAIL
        self.servidor_email = SMTP('smtp.gmail.com:587')
        self.servidor_email.ehlo()
        self.servidor_email.starttls()
        self.servidor_email.login(self.email, self.senha)

    def send_basic_email(self):
        if self.request.method == 'POST':
            form = self.request.POST
            if self.request.user.is_anonymous:
                to = form['email_to']
            else:
                to = self.request.user.email

            msg = MIMEMultipart('alternative')
            msg['Subject'] = 'Mensagem Praticando Django'
            msg['From'] = form['email']
            msg['To'] = to
            message = f'''<p>{form["name"]}, where you phone is {form["phone"]} and email {form['email']}.
Is send the fallowing message:
{form["message"]}
Tank You and Good Bye!</p>'''
            msg.attach(MIMEText(message, 'html'))
            self.servidor_email.sendmail(self.email, to, msg.as_string().encode('utf-8'))
            self.servidor_email.quit()

    def send_password(self, to, password):
        msg = MIMEMultipart('alternative')
        msg['Subject'] = 'Mensagem Praticando Django'
        msg['From'] = self.email
        msg['To'] = to
        message = f'''<p>The password of account is {password}</p>'''
        msg.attach(MIMEText(message, 'html'))
        self.servidor_email.sendmail(self.email, to, msg.as_string().encode('utf-8'))
        self.servidor_email.quit()