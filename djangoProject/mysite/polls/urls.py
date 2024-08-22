from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("main", views.index1, name="main"),
    path("class", views.index2, name="index2"),
    path("timings", views.index3, name="index3"),
    path("teachers", views.index4, name="index4"),
]