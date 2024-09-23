from django.urls import path
from .import views

urlpatterns=[
    path('', views.userLogin, name='userLogin'),
    path('index/', views.index, name='index'),
    path('registration/', views.registration, name='registration'),
    path('registerdata/', views.registerdata, name="registerdata"),
    # path('userData/', views.userData, name="userData")
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    
]