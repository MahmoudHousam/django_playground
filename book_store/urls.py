from django.urls import path
from . import views

urlpatterns = [
    path("first", view=views.index, name="index"),
    path("second", view=views.index2, name="index2"),
]
