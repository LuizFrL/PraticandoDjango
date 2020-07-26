from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from PraticandoDjango.Functions import AuthenticationValid
from apps.Usuarios.models import Profile


def login(request):
    if request.method == 'POST':
        data = {
            'username': request.POST['username'],
            'pass': request.POST['pass']
        }
        user = User.objects.filter(username=data['username'])
        if user.exists():
            user_auth = auth.authenticate(request, username=data['username'], password=data['pass'])
            if user_auth:
                auth.login(request, user_auth)
                return redirect('portifolio')
            messages.error(request, 'Senha incorreta', extra_tags='danger')
            return render(request, 'usuario/login/login.html', data)
        else:
            messages.error(request, 'Usuário incorreto ou não cadastrado.', extra_tags='danger')
            return render(request, 'usuario/login/login.html', data)
    return render(request, 'usuario/login/login.html')


def cadastro(request):
    if request.method == 'POST':
        form = request.POST
        if AuthenticationValid(request).valid_register_form(form):
            user = User.objects.create_user(
                username=form['username'],
                password=form['password1'],
                email=form['email'],
                first_name=form['name1'],
                last_name=form['name2']
            )

            perfil = Profile.objects.create(
                user=user,
                funcao=form['funcao'],
                foto_perfil=request.FILES['foto_perfil'],
                linkedin=form['linkedin'],
                git_hub=form['github']
            )
            user.save()
            perfil.save()
            messages.success(request, 'Usuário cadastrado com sucesso!', 'success')
            return redirect('login')
        return render(request, 'usuario/cadastro/cadastro.html', form)
    return render(request, 'usuario/cadastro/cadastro.html')


def logout(request):
    auth.logout(request)
    return redirect('preview')


def forgot(request):
    return render(request, 'usuario/login/forgot.html')
