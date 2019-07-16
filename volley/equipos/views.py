from django.http import HttpResponse
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from main.models import Persona, Equipo, Taller
from .forms import PersonaForm

@login_required
def index_equipo(request): # *args, **kwargs

    lista = []
    template_name = 'equipos/index.html'
    paginate_by = 40
    personas    = Persona.objects.filter(es_delete='False')
    equipos     = Equipo.objects.filter(es_delete='False').filter(es_interno=True)

    for equipo in equipos:
        jugadores=dict()
        cantidad=Persona.objects.filter(equipo_id=equipo.id).count()
        jugadores['equipo_id']=equipo.id
        jugadores['cantidad']=cantidad
        lista.append(jugadores)

    return render(request, template_name, {'personas': personas, 'equipos': equipos, 'jugadores': lista })

@login_required
def ver_equipo(request,pk):

    jugadores = Persona.objects.filter(equipo_id=pk)

    template = 'equipos/ver_equipo.html'

    return render(request, template, {'jugadores': jugadores })
