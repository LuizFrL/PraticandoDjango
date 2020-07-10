from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        user = User.objects.filter(username=username)
        if user.exists():
            user_auth = auth.authenticate(request, username=username, password=password)
            auth.login(request, user_auth)
            return redirect('portifolio')
        else:
            data = {
                'username': username,
                'pass': password
            }
            messages.error(request, 'Usuário ou senhas incorretos ou não cadastrados.', extra_tags='danger')
            return render(request, 'usuario/login/index.html', data)
    return render(request, 'usuario/login/index.html')


def cadastro(request):
    return None