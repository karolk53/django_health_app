from django.urls import path
from .views import register_user

app_name = 'register'

urlpatterns = [
    path('',register_user,name='registration')
]