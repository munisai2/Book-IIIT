from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="Home"),
    path("signup/",views.register,name="Register")
]
