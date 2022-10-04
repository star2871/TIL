from django.urls import path
from . import views

app_name = "articles"

ulpatterns = [
    path("", views.index, name="index"),
]
