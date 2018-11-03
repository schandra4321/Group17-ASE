
from django.urls import path, include
from . import views

urlpatterns = [

    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('create-auction/', views.create_auction, name = 'create-auction'),
    #path('enter-details/', views.enter_details, name = 'enter-details'),
    #path('dashboard/notifications/', views.notifications, name = 'notifications'),
    #path('dashboard/cart/', views.cart, name = 'cart'),
    #path('dashboard/created-auctions/', views.view_created, name = 'view-created'),
    #path('dashboard/participating-auctions/', views.view_participating, name = 'view-participating'),
]
