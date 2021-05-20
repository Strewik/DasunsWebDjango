from django.urls import path, include
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views #import this
from django.urls import reverse_lazy
from django.conf.urls.static import static
from django.conf import settings

app_name = "profiles"   

urlpatterns = [
    path('', views.main, name='homepage'),
    path('password_reset/', views.password_reset_request, name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="profiles/password/password_reset_done.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('profiles:password_reset_complete'), template_name="profiles/password/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="profiles/password/password_reset_complete.html"), name='password_reset_complete'),
    path('spregsave/', views.spreg_save, name='spregsave'),
    path('spreg/', views.spreg, name='spreg'),
    path('spregsuccess/', views.spregsuccess, name="spregsuccess"), 
    path('logout/', views.logout_request, name='logout'),
    path('caption/', views.captioningList, name='captioning'),
    path('intern/', views.internationalInterpList, name='international-interp'),
    path('mobguide/', views.mobGuideList, name='mobility-guide'),
    path('support/', views.personalSupportList, name='personal-support'),
    path('ugandan/', views.ugandanInterpList, name='ugandan-interp'),
    path('tactile/', views.tactileInterpList, name='tactile-interp'),
    path('booking/<str:pk>', views.createBooking, name="create_booking"),
    path('serviceuserdash/', views.serviceuserdash, name='serviceuserdash'),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('spdash/', views.serviceproviderdash, name="serviceproviderdash"),
    # path('addServiceuser/', views.addServiceuser, name="addServiceuser"),
    path('update_serviceuser/<str:pk>', views.updateServiceuser, name="update_serviceuser"),
    path('delete_serviceuser/<str:pk>', views.deleteServiceuser, name="delete_serviceuser"),
    path('update_serviceprovider/<str:pk>', views.updateServiceprovider, name="update_serviceprovider"),
    path('delete_serviceprovider/<str:pk>', views.deleteServiceprovider, name="delete_serviceprovider"),
    path('generalDash/', views.generalDash, name="generalDash"),
    path('profile/', views.serviceUserProfile, name="profile"),
    path('splist/', views.spList, name="splist"),
    path('profilesp/', views.serviceProviderProfile, name="profilesp"),
    path('updatebookingstatus/<str:pk>', views.updateBookingStatus, name="updatebookingstatus"),
    path('serviceuserdetails/', views.serviceUserDetails, name="serviceuserdetails"),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)