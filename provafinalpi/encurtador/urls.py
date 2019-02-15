"""encurtador URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from links.views import enviar_url, listar_url, desencurtar_url,api_encurtar_url,api_desencurtar_url,falha

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',enviar_url),
    path('listar/',listar_url, name='listar'),
    path('us/<slug:encurtado>',desencurtar_url),
    path('api/encurtar',api_encurtar_url.as_view(),name=api_encurtar_url.name),
    path('api/<slug:encurtado>',api_desencurtar_url.as_view(),name=api_desencurtar_url.name),
    path('falha',falha,name='falha')
]
