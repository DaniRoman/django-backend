from django.contrib import admin
from django.urls import path
from apps.store import views

urlpatterns = [
    path('store/', views.home_page, name='store'),
]
