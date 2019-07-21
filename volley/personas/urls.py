from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import PersonaList, PersonaCreate, PersonaUpdate, PersonaDelete

urlpatterns = [
    url(r'^$', PersonaList.as_view(), name='personas'),
    url(r'^new/$', PersonaCreate.as_view(), name='personas_new'),
    url(r'^editar/(?P<pk>\d+)/$', PersonaUpdate.as_view(), name='personas_edit'),
    url(r'^eliminar/(?P<pk>\d+)/$', PersonaDelete.as_view(), name='personas_delete'),
    ]    