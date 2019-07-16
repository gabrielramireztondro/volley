from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_equipo, name='equipos'),
    path('equipos/<int:pk>/ver/', views.ver_equipo, name='equipos_ver'),
    ]
