from django.urls import path
from . import views

app_name = "profiles"   

urlpatterns = [
    path('', views.main, name="homepage"),
    # path('client/', views.client),
    path('servicep/', views.serviceproviders),
    path('dashboard/', views.dashboard),
    path('serviceuser/', views.serviceuserdash, name="serviceuserdashboard"),
    path('spreg/', views.spreg, name="serviceproviderregister"),
    path('register/', views.register_request, name="register"),
    path('login/', views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout")
]



# urlpatterns = [
#     path("", views.homepage, name="homepage"),
#     ...
#     path("register", views.register_request, name="register")
# ]