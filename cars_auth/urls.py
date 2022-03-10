from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import UserDetailView, RegistrationView


urlpatterns = [
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'),
]
