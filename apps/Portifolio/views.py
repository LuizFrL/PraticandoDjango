from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.shortcuts import render, redirect

from apps.Usuarios.models import Profile


def portifolio_pessoal(request):
    if request.user.is_authenticated:
        data = {
            'perfil': get_object_or_404(Profile, pk=request.user.id)
        }
        return render(request, 'portifolio/portifolio_pessoal.html', data)
    return redirect('cadastro')


def preview(request):
    return render(request, 'portifolio/model_portifolio.html')