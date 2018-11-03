from django.urls import path, include
from Users import views

urlpatterns = [

    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('UpdateProfile/', views.UpdateProfile, name='UpdateProfile'),

]