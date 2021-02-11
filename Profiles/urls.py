from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('client/', views.client),
    path('serviceprovider/', views.serviceprovider),
    path('dashboard/', views.dashboard),
]

