from django.urls import path
from django.views.generic import TemplateView

app_name = 'main'

urlpatterns = [
    path('home/',TemplateView.as_view(template_name='main/home_page.html'),name='home_page')
]