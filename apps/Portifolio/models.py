from datetime import datetime

from django.contrib.auth.models import User
from django.db import models



def upload_to_item(instance, filename):
    return 'fotos/portifolio/item/{}/{}'.format(instance.user.id, filename)


def upload_to_portifolio(instance, filename):
    return 'fotos/portifolio/foto_perfil/{}/{}'.format(instance.user.id, filename)


# Create your models here.
class Portfolio(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=90)
    descricao = models.TextField()
    imagem = models.FileField(upload_to=upload_to_portifolio, blank=True)


class PortifolioItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=40)
    foto = models.ImageField(upload_to=upload_to_item, blank=True)
    descricao = models.TextField(max_length=200)
    data = models.DateField(default=datetime.today())
