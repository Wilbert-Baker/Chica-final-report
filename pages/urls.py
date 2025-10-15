from django.urls import path
from . import views


urlpatterns = [
    path("", views.home_view, name="root"),
    path("home/", views.home_view, name="home"),
    path("about_me/", views.home_view, name="about"),
]
