from django.urls import path
from . import views

urlpatterns = [
    path("",views.homePage,name="Home"),
    path("signup/",views.registerPage,name="Register")
]
