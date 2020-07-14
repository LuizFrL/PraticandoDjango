from smtplib import SMTP
from typing import Dict, Union, Tuple

from django.contrib import messages
from django.contrib.auth.models import User


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

    def send_basic_email(self):
        if self.request.method == 'POST':
            form = self.request.POST

            print("Enviando email.")
            email = 'extremobr001@gmail.com'
            senha = 'UM2&9D7K'
            servidor_email = SMTP('smtp.gmail.com:587')
            servidor_email.ehlo()
            servidor_email.starttls()
            servidor_email.login(email, senha)

            msg = MIMEMultipart('alternative')
            msg['Subject'] = f'[Monitoramento de envio de notas fiscais] Controle diário'
            msg['From'] = email
            msg['To'] = grupo

            servidor_email.sendmail(email, grupo, form[''])
