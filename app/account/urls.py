from rest_framework import routers

from django.urls import path, include
from django.contrib.auth import views as auth_views

from .views import UserViewSet

app_name = 'account'

router = routers.DefaultRouter()
router.register('list', UserViewSet)

urlpatterns = [
    path('accounts/', include(router.urls)),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', auth_views.LogoutView.as_view(), name='logout'),
]
