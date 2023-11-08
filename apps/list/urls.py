from django.urls import path
from apps.list.views import home

urlpatterns = [
    path('', home, name='list'),
]