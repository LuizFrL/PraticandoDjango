from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Portfolio(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=90)
    descricao = models.TextField()
    imagem = models.FileField(upload_to='fotos/portifolio/%d/%m/%Y/', blank=True)
