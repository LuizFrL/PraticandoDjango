from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect


def portifolio_pessoal(request):
    if request.user.is_authenticated:
        data = {
            '': ''
        }
        return render(request, 'usuario/../../templates/portifolio/portifolio_pessoal.html', data)
    return redirect('cadastro')


def preview(request):
    return render(request, 'portifolio/model_portifolio.html')