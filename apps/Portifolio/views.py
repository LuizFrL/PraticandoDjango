import os

from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.shortcuts import render, redirect

from PraticandoDjango import settings
from PraticandoDjango.Functions import SendEmail
from apps.Portifolio.models import PortifolioItem, SobreVoce
from apps.Usuarios.models import Profile


def create_item(request):
    form = request.POST
    portifolio_item = PortifolioItem.objects.create(
        user_id=request.user.id,
        titulo=form['titulo'],
        foto=request.FILES['foto'],
        descricao=form['descricao']
    )
    portifolio_item.save()


def delete_media(portifolio: PortifolioItem):
    os.remove(portifolio.foto.path)
    print('deletado')


def portifolio_pessoal(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.POST.get('delete'):
                try:
                    portifolio: PortifolioItem = get_object_or_404(PortifolioItem, pk=request.POST.get('delete'))
                    delete_media(portifolio)
                    portifolio.delete()
                except:
                    pass
            else:
                create_item(request)
        portifolio_list = PortifolioItem.objects.order_by('-data').filter(user_id=request.user.id)
        sobre_voce_list = SobreVoce.objects.filter(user_id=request.user.id)

        # print([portifolio_list[i:i + 3] for i in range(0, len(portifolio_list), 3)])
        data = {
            'perfil': get_object_or_404(Profile, pk=request.user.id),
            'portifolios': portifolio_list,
            'sobre_voce': sobre_voce_list
        }
        return render(request, 'portifolio/portifolio_pessoal.html', data)
    return redirect('cadastro')


def preview(request):
    return render(request, 'portifolio/model_portifolio.html')


def contato(request):
    SendEmail(request).send_basic_email()
    return redirect('portifolio')


def sobre_voce(request):
    return redirect('portifolio')