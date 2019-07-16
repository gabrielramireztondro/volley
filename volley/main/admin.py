from django.contrib import admin
from .models import Pais, SistemaSalud, EstadoCivil, Genero, Club, Posicion, Taller, Persona, Periodo, Dia, EstadoClase, Gimnacio, Plan
from .models import Region, Provincia, Comuna, Equipo
@admin.register(SistemaSalud)
class ComentAdmin(admin.ModelAdmin):
    list_display=('descripcion','es_activo','es_delete','fecha_crea','fecha_modi')

@admin.register(EstadoCivil)
class ComentAdmin(admin.ModelAdmin):
    list_display=('descripcion','es_activo','es_delete','fecha_crea','fecha_modi')

@admin.register(Genero)
class ComentAdmin(admin.ModelAdmin):
    list_display=('descripcion','es_activo','es_delete','fecha_crea','fecha_modi')

@admin.register(Club)
class ComentAdmin(admin.ModelAdmin):
    list_display=('descripcion','es_activo','es_delete','fecha_crea','fecha_modi')

@admin.register(Taller)
class ComentAdmin(admin.ModelAdmin):
    list_display=('descripcion','es_activo','es_delete','fecha_crea','fecha_modi')

@admin.register(Posicion)
class ComentAdmin(admin.ModelAdmin):
    list_display=('descripcion','es_activo','es_delete','fecha_crea','fecha_modi')

@admin.register(Persona)
class ComentAdmin(admin.ModelAdmin):
    list_display=('dna','nombres','apellido_paterno','apellido_materno','es_activo','es_delete','fecha_crea','fecha_modi')

@admin.register(Periodo)
class ComentAdmin(admin.ModelAdmin):
    list_display=('periodo','es_activo','es_delete','fecha_crea','fecha_modi')

@admin.register(Dia)
class ComentAdmin(admin.ModelAdmin):
    list_display=('abreviatura','descripcion','es_activo','es_delete','fecha_crea','fecha_modi')

@admin.register(EstadoClase)
class ComentAdmin(admin.ModelAdmin):
    list_display=('descripcion','es_activo','es_delete','fecha_crea','fecha_modi')

@admin.register(Gimnacio)
class ComentAdmin(admin.ModelAdmin):
    list_display=('descripcion','es_activo','es_delete','fecha_crea','fecha_modi')

@admin.register(Pais)
class ComentAdmin(admin.ModelAdmin):
    list_display=('descripcion','es_activo','fecha_crea','fecha_modi')

@admin.register(Region)
class ComentAdmin(admin.ModelAdmin):
    list_display=('descripcion','es_activo','fecha_crea','fecha_modi')

@admin.register(Provincia)
class ComentAdmin(admin.ModelAdmin):
    list_display=('descripcion','es_activo','fecha_crea','fecha_modi')

@admin.register(Comuna)
class ComentAdmin(admin.ModelAdmin):
    list_display=('descripcion','es_activo','fecha_crea','fecha_modi')


@admin.register(Equipo)
class ComentAdmin(admin.ModelAdmin):
    list_display=('descripcion','es_activo','fecha_crea','fecha_modi')
