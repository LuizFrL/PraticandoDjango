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
