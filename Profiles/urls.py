from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('client/', views.client),
    path('serviceprovider/', views.serviceprovider),
    path('dasuns/', views.dasuns),
]

