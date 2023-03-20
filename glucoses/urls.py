from django.urls import path
from .views import add_measurement,measurement_list
from django.views.generic import TemplateView

app_name = 'glucoses'

urlpatterns = [
    path('',TemplateView.as_view(template_name='glucoses/menu.html'),name='menu'),
    path('add/',add_measurement,name='add'),
    path('list/',measurement_list,name='list'),
]