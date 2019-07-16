from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='personas'),
    path('personas/new/', views.personas_new, name='personas_new'),
    path('personas/<int:pk>/edit/', views.personas_edit, name='personas_edit'),
    path('personas/<int:pk>/delete/', views.personas_delete, name='personas_delete'),
    ]    
