# cold_emailing/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import EmailInterfaceView

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'campaigns', views.CampaignViewSet)
router.register(r'emails', views.EmailViewSet)
router.register(r'contacts', views.ContactViewSet)
router.register(r'campaign_contacts', views.CampaignContactViewSet)
router.register(r'email_settings', views.EmailSettingsViewSet)

urlpatterns = [
    path('login/', views.login_view, name='login_view'),
    path('', include(router.urls)),
    path('email_interface/', EmailInterfaceView.as_view(), name='Send Mail'),
]