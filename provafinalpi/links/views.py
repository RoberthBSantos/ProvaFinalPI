import random

from django.core.checks import messages
from rest_framework import generics
from django.shortcuts import render, redirect
import string

# Create your views here.
from links.forms import LinkForm
from links.models import Link
from links.serializers import LinkSerializer, LinkDesencurtadoSerializer


def listar_url(request):
    links = Link.objects.all()
    return render(request, "listar_urls.html", {'links':links})

def enviar_url(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            link = Link
            link.original = form.cleaned_data['original']
            link.encurtado = random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)
            if(len(link.encurtado)>len(link.original)):
                return redirect('falha')
            Link.encurtar(link,link.original,link.encurtado)
            return redirect('listar')
    else:
        form = LinkForm()
        return render(request, "encurtar.html" ,{'form': form})

def falha(request):
    return render(request,'falha.html')


def desencurtar_url(request,encurtado):
    print(encurtado)
    link = Link.objects.get(encurtado=encurtado)
    redirecinar = link.original
    return redirect(redirecinar)


class api_encurtar_url(generics.CreateAPIView):
    serializer_class = LinkSerializer
    name = 'api-encurtar'
    queryset = Link.objects.all()


class api_desencurtar_url(generics.RetrieveAPIView):
    serializer_class = LinkDesencurtadoSerializer
    name = 'api-desencurtar'
    queryset = Link.objects.all()
    lookup_field = 'encurtado'
