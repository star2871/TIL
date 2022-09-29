from django.urls import path
from . import views

app_name = "day5"


urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("change/<int:pk_>", views.change, name="change"),
    path("delete/<int:pk>", views.delete, name="delete"),
]
