from django.shortcuts import render, get_object_or_404
from .models import Item

# Create your views here.
from django.http import HttpResponse


def home(request):
    return render(request, "coffeemachine/home.html")


def detail(request, name):
    item = get_object_or_404(Item, name=name)

    return render(request, "coffeemachine/detail.html", {"item": item})
