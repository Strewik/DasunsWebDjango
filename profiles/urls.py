from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('client/', views.client),
    path('serviceprovider/', views.serviceprovider),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('spreg/', views.spreg),
    path('sps/', views.sps),
    path('client/', views.client),

    path('serviceuser/', views.serviceuser, name="serviceusers"),
    path('update_serviceuser/<str:pk>', views.updateServiceuser, name="update_serviceuser"),
    path('delete_serviceuser/<str:pk>', views.deleteServiceuser, name="delete_serviceuser"),
]

