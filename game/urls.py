from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.start_game, name='start_game'),
    path('home/',views.home,name='home'),


]