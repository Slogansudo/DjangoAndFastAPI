from django.urls import path
from .views import LoginView, UserRegisterView, AddressView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('address/', AddressView.as_view(), name='address')
]
