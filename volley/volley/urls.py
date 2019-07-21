from django.contrib import admin
from django.urls import include, path, reverse_lazy
from django.conf.urls import url
from main.views import home_view

urlpatterns = [
    path('login/', include('login.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('',home_view, name='home'),
    path('personas/', include('personas.urls')),
    path('equipos/', include('equipos.urls')),
]
