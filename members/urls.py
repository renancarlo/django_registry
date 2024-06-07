from django.urls import path

from . import views

# app_name = "members"
urlpatterns = [
    path("", views.main, name="main"),
    path("register", views.register, name="register"),
    path("all/",views.view_allmembers, name="all"),
    path("all/details/<int:id>",views.view_details, name="details"),
    path("testing/", views.testing, name="testing"),
]