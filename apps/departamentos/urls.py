from django.contrib import admin
from django.urls import path, include

from .views import (DepartamentosList,
                    DepartamentoCreate,
                    DepartamentoUpdate,
                    DepartamentoDelete)
urlpatterns = [
    path('list', DepartamentosList.as_view(), name='list_departamentos'),
    path('create', DepartamentoCreate.as_view(), name='create_departamentos'),
    path('update/<int:pk>', DepartamentoUpdate.as_view(), name='update_departamentos'),
    path('delete/<int:pk>', DepartamentoDelete.as_view(), name='delete_departamentos'),
]
