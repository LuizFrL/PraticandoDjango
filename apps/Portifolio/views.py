from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.shortcuts import render, redirect

from apps.Portifolio.models import PortifolioItem
from apps.Usuarios.models import Profile


def create_item(request):
    form = request.POST
    print(form)
    portifolio_item = PortifolioItem.objects.create(
        user_id=request.user.id,
        titulo=form['titulo'],
        foto=request.FILES['foto'],
        descricao=form['descricao']
    )
    portifolio_item.save()


def portifolio_pessoal(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            create_item(request)
        data = {
            'perfil': get_object_or_404(Profile, pk=request.user.id),
            'portifolios': PortifolioItem.objects.order_by('-data').filter(user_id=request.user.id)
        }
        print(data)
        return render(request, 'portifolio/portifolio_pessoal.html', data)
    return redirect('cadastro')


def preview(request):
    return render(request, 'portifolio/model_portifolio.html')

