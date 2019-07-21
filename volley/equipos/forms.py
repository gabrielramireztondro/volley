from django.db import models
from django.forms import ModelForm
from django import forms
from bootstrap_datepicker_plus import DatePickerInput
from main.models import Equipo


class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        exclude = ('es_delete','fecha_crea','fecha_modi')

        widgets = {
            'fecha_nacimiento': DatePickerInput(format='%Y-%m-%d'), # python date-time format

            'dna': forms.TextInput(attrs={'size': 12, 'width': 12}),

        }
