from django.urls import path
from .import views

urlpatterns=[
    path('', views.login, name='login'),
    # path('index/', views.index, name='index'),
    path('registration/', views.registration, name='registration'),
    # path('registerdata/', views.registerdata, name="registerdata"),
    # path('userData/', views.userData, name="userData")
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('logout/', views.logout, name="logout"), 
    path('linkedin/', views.linkedin, name="linkedin"),
    path('instagram/', views.instagram, name="instagram"),
    path('github/', views.github, name="github"),
    # path('email/', views.email, name="email"),
    
]