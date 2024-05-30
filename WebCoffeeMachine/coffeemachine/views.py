from django.shortcuts import get_object_or_404, render

from .models import Item


def home(request):
    return render(request, "coffeemachine/home.html")


def detail(request, name):
    item = get_object_or_404(Item, name=name)
    context = {"item": item}
    return render(request, "coffeemachine/detail.html", context)
