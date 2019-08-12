from django.http import HttpResponse
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from main.models import Equipo, Persona
from .forms import PersonaForm
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView, TemplateView

@login_required
def index_equipo(request): # *args, **kwargs

    lista = []
    template_name = 'equipos/index.html'
    paginate_by = 10
    personas    = Persona.objects.filter(es_delete='False')
    equipos     = Equipo.objects.filter(es_delete='False').filter(es_interno=True).filter(club=1)

    for equipo in equipos:
        jugadores=dict()
        cantidad=Persona.objects.filter(equipo_id=equipo.id).count()
        jugadores['equipo_id']=equipo.id
        jugadores['cantidad']=cantidad
        lista.append(jugadores)

    return render(request, template_name, {'personas': personas, 'equipos': equipos, 'jugadores': lista })

class EquiposListView(ListView):
    template_name = 'equipos/lista_equipos.html'

    def get_queryset(self,**kwargs):
        id_equipo=self.kwargs.get("id")
        return Persona.objects.filter(equipo_id=id_equipo)

    def get_context_data(self, **kwargs):
        context = super(EquiposListView, self).get_context_data(**kwargs)
        context['equipo'] = Equipo.objects.filter(id=self.kwargs['id'])
        return context


def QuitardeEquipo(request, id):
    lista = []
    template_name = 'equipos/index.html'

    personas    = Persona.objects.filter(es_delete='False')
    equipos     = Equipo.objects.filter(es_delete='False').filter(es_interno=True).filter(club=1)
    jugador     = Persona.objects.get(id=id)
    jugador.equipo_id=6
    jugador.save()

    for equipo in equipos:
        jugadores=dict()
        cantidad=Persona.objects.filter(equipo_id=equipo.id).count()
        jugadores['equipo_id']=equipo.id
        jugadores['cantidad']=cantidad
        lista.append(jugadores)

    return render(request, template_name, {'personas': personas, 'equipos': equipos, 'jugadores': lista })

class AgregarJugadores(TemplateView):
    template_name = 'equipos/agregar_jugadores.html'

    def get_context_data(self, *args, **kwargs):
        context = super(AgregarJugadores, self).get_context_data(*args, **kwargs)
        context['equipo'] = Equipo.objects.filter(id=self.kwargs['id'])
        return context    

def ListarJugadores(request):
    lista=serializers.serialize('json',Persona.objects.all())
    return HttpResponse(lista, content_type='application/json' )

#https://es.stackoverflow.com/questions/108912/c%C3%B3mo-usar-dos-o-m%C3%A1s-modelos-para-listar-en-un-template-django