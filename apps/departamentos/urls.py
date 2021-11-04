from django.contrib import admin
from django.urls import path, include

from .views import DepartamentosList
urlpatterns = [
    path('list', DepartamentosList.as_view(), name='list_departamentos'),
]
