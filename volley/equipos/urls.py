from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import index_equipo,EquiposListView,QuitardeEquipo, AgregarJugadores, ListarJugadores

urlpatterns = [
    url(r'^$', index_equipo, name='equipos'),
    path('<int:id>/', EquiposListView.as_view(), name='equipos_list'),
    url(r'^quitar/(?P<id>\d+)$', QuitardeEquipo, name='abandona_equipo'),
    url(r'^agregar/(?P<id>\d+)$', AgregarJugadores.as_view(), name='agregar_jugadores'),  
    url(r'^listar/', ListarJugadores, name='listar_jugadores'),   
    ]    