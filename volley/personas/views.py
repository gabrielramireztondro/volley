from django.http import HttpResponse
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from main.models import Persona
from .forms import PersonaForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView



class PersonaList(ListView):
    model = Persona
    template_name = 'personas/index.html'
    paginate_by = 10
    
class PersonaCreate(CreateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'personas/new.html'
    success_url = reverse_lazy('personas')

class PersonaUpdate(UpdateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'personas/edit.html'
    success_url = reverse_lazy('personas')


class PersonaDelete(DeleteView):
    model = Persona
    template_name = 'personas/delete.html'
    success_url = reverse_lazy('personas')
