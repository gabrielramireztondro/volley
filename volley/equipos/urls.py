from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import index_equipo,EquiposList

urlpatterns = [
    url(r'^$', index_equipo, name='equipos'),
    url(r'^listar/(?P<pk>\d+)/$', EquiposList.as_view(), name='equipos_list'),
    ]    