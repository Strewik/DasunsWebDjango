from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('client/', views.client),
    path('serviceprovider/', views.serviceprovider),
    path('dashboard/', views.dashboard),
    path('serviceuser/', views.serviceuserdash),
    path('spreg/', views.spreg),
    path('signuplogin/', views.signuplogin),
    path('signup/', views.signup),
    path('login/', views.login),
]

