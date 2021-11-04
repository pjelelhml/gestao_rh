from django.contrib import admin
from django.urls import path, include

from .views import FuncionariosList, FuncionarioEdit, FuncionarioDelete

urlpatterns = [
    path('', FuncionariosList.as_view(), name='list_funcionarios'),
    path('edita/<int:pk>', FuncionarioEdit.as_view(), name='update_funcionario'),
    path('delete/<int:pk>', FuncionarioDelete.as_view(), name='delete_funcionario'),

]
