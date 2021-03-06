from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('logout', views.logout, name='logout'),
    path('forgot', views.forgot, name='forgot_password'),
]
