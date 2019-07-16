from django.http import HttpResponse
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from main.models import Persona
from .forms import PersonaForm

@login_required
def index_view(request): # *args, **kwargs

    model = Persona
    template_name = 'personas/index.html'
    paginate_by = 40
    personas = Persona.objects.filter(es_delete='False')
    return render(request, template_name, {'personas': personas})

@login_required
def personas_new(request):
    if request.method=='POST':
        page = 'personas/index.html'
        #Formulario Enviado
        form = PersonaForm(request.POST or None)
        if form.is_valid():
            # Formulario OK
            form.save()
            return redirect('personas')
            # redirigir a la pagina de detall
        else:
            form = PersonaForm(request.POST or None)
            context = {
                'form': form,
            }
    else:
        form = PersonaForm()
        page = 'personas/new.html'
        context = {
            'form': form,
        }

    return render(request, page, context)


@login_required
def personas_edit(request,pk):

    post = get_object_or_404(Persona, id=pk)
    form = PersonaForm(request.POST or None, instance=post)
    context = {'form': form,}
    page = 'personas/index.html'

    if request.method=='POST':
        #Formulario Enviado
        form = PersonaForm(request.POST or None, instance=post)

        if form.is_valid():
            # Formulario OK
            form.save()

            return redirect('personas')

        else:
            form = PersonaForm(request.POST or None, instance=post)
            context = {'form': form,}
            page = 'personas/index.html'
    else:
        print("editando esta wea")
        form = PersonaForm(instance=post)
        page = 'personas/edit.html'
        context = {'form': form,}

    return render(request, page, context)

@login_required
def personas_delete(request,pk):

    post = get_object_or_404(Persona, id=pk)
    form = PersonaForm(request.POST or None, instance=post)
    context = {'form': form,}
    page = 'personas/index.html'

    if request.method=='POST':
        #Formulario Enviado
        form = PersonaForm(request.POST or None, instance=post)

        if form.is_valid():
            # Formulario OK
            form.save()

            return redirect('personas')

        else:
            form = PersonaForm(request.POST or None, instance=post)
            context = {'form': form,}
            page = 'personas/index.html'
    else:
        form = PersonaForm(instance=post)
        page = 'personas/edit.html'
        context = {'form': form,}

    return render(request, page, context)
