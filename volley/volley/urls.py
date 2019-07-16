from django.contrib import admin
from django.urls import include, path
from main.views import home_view
from equipos.views import index_equipo
urlpatterns = [
    path('equipos/', include('equipos.urls')),
    path('personas/', include('personas.urls')),
    path('login/', include('login.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('', index_equipo, name='equipo'),

]
