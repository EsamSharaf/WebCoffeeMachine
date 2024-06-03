from django.http import HttpResponse
from django.views.generic import ListView
from .models import Item


class HomeListView(ListView):
    model = Item
    template_name = "coffeemachine/home.html"


def detail(request, name):
    return HttpResponse("You're looking at item %s detail page." % name)
