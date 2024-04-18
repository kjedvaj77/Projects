from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/", views.fail, name="wiki"),
    path("wiki/<str:title>/", views.title, name="title"),
    path("search/", views.search, name="q"),
    path("new/", views.new, name="new_page"),
    path("edit/", views.edit, name="edit"),
    path("sucess/", views.confrim, name="sucess"),
    path("random/", views.random, name="random")
]
