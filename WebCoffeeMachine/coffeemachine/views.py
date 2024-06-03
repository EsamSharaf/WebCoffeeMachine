from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Item


class HomeListView(ListView):
    model = Item
    template_name = "coffeemachine/home.html"


class ItemDetailPage(DetailView):
    model = Item
    pk_url_kwarg = 'name'
    template_name = "coffeemachine/detail.html"
