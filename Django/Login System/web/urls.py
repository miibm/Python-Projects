from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.loginpage,name='loginpage'),
    path('register/',views.registerpage,name='registerpage'),
    path('logout/',views.logoutpage,name='logoutpage'),
]