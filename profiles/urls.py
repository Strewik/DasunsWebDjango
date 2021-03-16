from django.urls import path, include
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views #import this
from django.urls import reverse_lazy

app_name = "profiles"   

urlpatterns = [
    path('', views.main, name='homepage'),
    path('password_reset/', views.password_reset_request, name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="profiles/password/password_reset_done.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('profiles:password_reset_complete'), template_name="profiles/password/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="profiles/password/password_reset_complete.html"), name='password_reset_complete'),
    path('spreg/', views.spreg, name='servicep'),
    path("logout", views.logout_request, name='logout'),
    path("booking/", views.booking, name='booking'),
    path('serviceprovider/', views.serviceprovider),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('sps/', views.sps),
    path('serviceuser/', views.serviceuser, name="serviceusers"),
    path('update_serviceuser/<str:pk>', views.updateServiceuser, name="update_serviceuser"),
    path('delete_serviceuser/<str:pk>', views.deleteServiceuser, name="delete_serviceuser"),

]

