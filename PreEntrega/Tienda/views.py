from django.shortcuts import render
from Tienda.models import Registro
from Tienda.models import Carrito
from Tienda.models import Productos
from django.http import HttpResponse
from django.template import loader


# Create your views here.


def inicio(request):
    return render(request, "home.html")

def nosotros(request):
    return render(request, "nosotros.html")

def products(request):
    return render(request, "productos.html")

def login(request):
    return render(request, "login.html")