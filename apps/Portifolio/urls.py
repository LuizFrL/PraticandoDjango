from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views

urlpatterns = [
    path('index', views.portifolio_pessoal, name='portifolio'),
    path('', views.preview, name='preview'),
    path('contato', views.contato, name='contato'),
]
