from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
]

# urlpatterns = [
#     path('', views.index, name='index'),
# ]