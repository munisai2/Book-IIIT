from django.urls import path
from scheduling import views


urlpatterns = [
    path("",views.homePage,name="Home"),
    path("signup/",views.registerPage,name="Register"),
    path("login/",views.loginPage,name="Register"),
    path("Booking/",views.booking_details,name="Booking_Details"),
    

]
