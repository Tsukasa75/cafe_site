from django.urls import path, include
from .import views

app_name= 'cafe_site'

urlpatterns = [
    path('', views.index, name='index' )
]
