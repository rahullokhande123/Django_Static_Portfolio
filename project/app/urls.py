from django.urls import path
from .import views

urlpatterns=[
    path('', views.userLogin, name='userLogin'),
    path('home/', views.home, name='home'),
    path('registration/', views.registration, name='registration'),
    path('registerdata/', views.registerdata, name="registerdata"),
    
]