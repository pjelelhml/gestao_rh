from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from apps.core import views

from apps.funcionarios.api.serializers import FuncionarioSerializer
from apps.funcionarios.api.views import FuncionarioViewSet

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'api/funcionarios', FuncionarioViewSet)

urlpatterns = [
    path('', include('apps.core.urls')),
    path('funcionarios/', include('apps.funcionarios.urls')),
    path('documentos/', include('apps.documentos.urls')),
    path('departamen/', include('apps.departamentos.urls')),
    path('empresa/', include('apps.empresas.urls')),
    path('horas_extras/', include('apps.registro_hora_extra.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),

    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
