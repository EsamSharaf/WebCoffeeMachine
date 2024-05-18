from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    return render(request, "coffeemachine/home.html")


def detail(request, name):
    return HttpResponse("You're looking at item %s detail page." % name)
