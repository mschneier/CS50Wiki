from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<title>", views.wiki, name="wiki"),
    path(r"^search/(?P<query>\w{0,99})/$", views.search, name="search"),
    path("new/", views.new, name="new"),
    path("edit/<title>", views.edit, name="edit"),
    path("random/", views.random, name="random"),
]
