from django.db import models
from django.contrib.auth.models import User


class Profile(User):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE, parent_link=True, default=None)
    funcao = models.CharField(max_length=90)
    foto_perfil = models.ImageField(upload_to='fotos/perfil/%d/%m/%Y/', blank=True)
    linkedin = models.URLField(blank=True)
    git_hub = models.URLField(blank=True)
