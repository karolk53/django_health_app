from django.urls import path
from .views import add_survey,surveys_list,menu

app_name = 'bloodpresures'

urlpatterns = [
    path('',menu,name='menu'),
    path('add/',add_survey,name='add'),
    path('list/',surveys_list,name='list'),
]