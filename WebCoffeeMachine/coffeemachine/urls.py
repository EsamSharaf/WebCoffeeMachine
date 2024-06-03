from django.urls import path

from . import views

app_name = "coffeemachine"
urlpatterns = [
    path("", views.HomeListView.as_view(), name="home"),
    # ex: /coffeemachine/Black Coffee/
    path("<str:name>/", views.detail, name="detail"),
]
