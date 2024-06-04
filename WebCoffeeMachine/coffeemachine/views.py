from django.views.generic import DetailView, ListView

from .models import Item


class HomeListView(ListView):
    model = Item
    template_name = "coffeemachine/home.html"


class ItemDetailPage(DetailView):
    model = Item
    slug_url_kwarg = 'slug'
    template_name = "coffeemachine/detail.html"
