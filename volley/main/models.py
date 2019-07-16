from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

def get_default_my_hour():
    hour = timezone.now()
    formatedHour = hour.strftime("%H:%M:%S")
    return formatedHour

class Basetable(models.Model):

    es_delete           = models.BooleanField(default=False)
    es_activo           = models.BooleanField(default=True)
    fecha_crea          = models.DateTimeField(auto_now_add=True, help_text=("creation date"))
    fecha_modi          = models.DateTimeField(auto_now=True, null= True)

    class Meta:
        abstract=True

class Tabla(Basetable):
    id = models.AutoField(primary_key=True)
    descripcion         = models.CharField(blank=False, null=False, max_length=250)

    class Meta:
        verbose_name_plural="Tabla"
        db_table="tabla"

    def __str__(self):
        return self.descripcion

    def delete(self):
        if not self.es_delete:
            return False
        else:
            self.es_delete=True
            self.save()
            return True


class Pais(models.Model):

    id                  = models.AutoField(primary_key=True)
    alias               = models.CharField(blank=False, null=False, max_length=5)
    descripcion         = models.CharField(blank=False, null=False, max_length=150)
    nacionalidad        = models.CharField(blank=False, null=False, max_length=150)
    es_limitrofe        = models.BooleanField(default=False)
    es_activo           = models.BooleanField(default=True)
    fecha_crea          = models.DateField(default=timezone.now, help_text=("creation date"))
    fecha_modi          = models.DateField(auto_now=True, null= True)

    class Meta:
        verbose_name_plural="Paises"
        db_table="pais"

    def __str__(self):
        return self.descripcion

    def delete(self):
        pass


class Region(models.Model):

    id                  = models.AutoField(primary_key=True)
    descripcion         = models.CharField(blank=False, null=False, max_length=255)
    pais                = models.ForeignKey(Pais,null=True, on_delete=models.DO_NOTHING,verbose_name="Pais")
    es_activo           = models.BooleanField(default=True)
    fecha_crea          = models.DateField(default=timezone.now, help_text=("creation date"))
    fecha_modi          = models.DateField(auto_now=True, null= True, help_text=("creation modify"))

    class Meta:
        verbose_name_plural="Regiones"
        db_table="region"

    def __str__(self):
        return self.descripcion

    def delete(self):
        pass

class Provincia(models.Model):

    id                  = models.AutoField(primary_key=True)
    descripcion         = models.CharField(blank=False, null=False, max_length=255)
    region              = models.ForeignKey(Region,null=True, on_delete=models.DO_NOTHING,verbose_name="Region")
    es_activo           = models.BooleanField(default=True)
    fecha_crea          = models.DateField(default=timezone.now, help_text=("creation date"))
    fecha_modi          = models.DateField(auto_now=True, null= True, help_text=("creation modify"))

    class Meta:
        verbose_name_plural="Provincias"
        db_table="provincia"
    def __str__(self):
        return self.descripcion

    def delete(self):
        pass


class Comuna(models.Model):

    id                  = models.AutoField(primary_key=True)
    descripcion         = models.CharField(blank=False, null=False, max_length=255)
    provincia           = models.ForeignKey(Provincia,null=True, on_delete=models.DO_NOTHING,verbose_name="Provincia")
    es_capital          = models.BooleanField(default=False)
    es_activo           = models.BooleanField(default=True)
    fecha_crea          = models.DateField(default=timezone.now, help_text=("creation date"))
    fecha_modi          = models.DateField(auto_now=True, null= True, help_text=("creation modify"))

    class Meta:
        verbose_name_plural="Comunas"
        db_table="comuna"

    def __str__(self):
        return self.descripcion

    def delete(self):
        pass


class SistemaSalud(models.Model):

    id                  = models.AutoField(primary_key=True)
    descripcion         = models.CharField(blank=False, null=False, max_length=255)
    es_activo           = models.BooleanField(default=True)
    es_delete           = models.BooleanField(default=False)
    fecha_crea          = models.DateField(default=timezone.now, help_text=("creation date"))
    fecha_modi          = models.DateField(auto_now=True, null= True)

    class Meta:
        verbose_name_plural="Sistema Salud"
        db_table="sistema_salud"

    def __str__(self):
        return self.descripcion

    def delete(self):
        pass

class Genero(models.Model):

    id                  = models.AutoField(primary_key=True)
    descripcion         = models.CharField(blank=False, null=False, max_length=255, unique=True)
    es_activo           = models.BooleanField(default=True)
    es_delete           = models.BooleanField(default=False)
    fecha_crea          = models.DateField(default=timezone.now, help_text=("creation date"))
    fecha_modi          = models.DateField(auto_now=True, null= True)

    class Meta:
        verbose_name_plural="Generos"
        db_table="genero"

    def __str__(self):
        return self.descripcion

    def delete(self):
        pass

class EstadoCivil(models.Model):

    id                  = models.AutoField(primary_key=True)
    descripcion         = models.CharField(blank=False, null=False, max_length=255)
    es_activo           = models.BooleanField(default=True)
    es_delete           = models.BooleanField(default=False)
    fecha_crea          = models.DateField(default=timezone.now, help_text=("creation date"))
    fecha_modi          = models.DateField(auto_now=True, null= True)

    class Meta:
        verbose_name_plural="Estado Civil"
        db_table="estado_civil"

    def __str__(self):
        return self.descripcion

    def delete(self):
        pass

class Club(models.Model):

    id                  = models.AutoField(primary_key=True)
    descripcion         = models.CharField(blank=False, null=False, max_length=255, unique=True)
    es_activo           = models.BooleanField(default=True)
    es_delete           = models.BooleanField(default=False)
    fecha_crea          = models.DateField(default=timezone.now, help_text=("creation date"))
    fecha_modi          = models.DateField(auto_now=True, null= True)

    class Meta:
        verbose_name_plural="Clubes"
        db_table="club"

    def __str__(self):
        return self.descripcion

    def delete(self):
        pass

class Taller(models.Model):

    id                  = models.AutoField(primary_key=True)
    descripcion         = models.CharField(blank=False, null=False, max_length=255, unique=True)
    es_activo           = models.BooleanField(default=True)
    es_delete           = models.BooleanField(default=False)
    fecha_crea          = models.DateField(default=timezone.now, help_text=("creation date"))
    fecha_modi          = models.DateField(auto_now=True, null= True)

    class Meta:
        verbose_name_plural="Talleres"
        db_table="taller"

    def __str__(self):
        return self.descripcion

    def delete(self):
        pass

class Posicion(models.Model):

    id                  = models.AutoField(primary_key=True)
    descripcion         = models.CharField(blank=False, null=False, max_length=255, unique=True)
    es_activo           = models.BooleanField(default=True)
    es_delete           = models.BooleanField(default=False)
    fecha_crea          = models.DateField(default=timezone.now, help_text=("creation date"))
    fecha_modi          = models.DateField(auto_now=True, null= True)

    class Meta:
        verbose_name_plural="Posiciones"
        db_table="posicion"

    def __str__(self):
        return self.descripcion

    def delete(self):
        pass

class Periodo(models.Model):

    id                  = models.AutoField(primary_key=True)
    periodo             = models.IntegerField(blank=False, null=False)
    es_activo           = models.BooleanField(default=True)
    es_delete           = models.BooleanField(default=False)
    fecha_crea          = models.DateField(default=timezone.now, help_text=("creation date"))
    fecha_modi          = models.DateField(auto_now=True, null= True)

    class Meta:
        verbose_name_plural="Periodos"
        db_table="periodo"

    def __str__(self):
        return str(self.periodo)

    def delete(self):
        pass

class Dia(models.Model):

    id                  = models.AutoField(primary_key=True)
    abreviatura         = models.CharField(blank=False, null=False, max_length=4, unique=True)
    descripcion         = models.CharField(blank=False, null=False, max_length=255, unique=True)
    es_activo           = models.BooleanField(default=True)
    es_delete           = models.BooleanField(default=False)
    fecha_crea          = models.DateField(default=timezone.now, help_text=("creation date"))
    fecha_modi          = models.DateField(auto_now=True, null= True)

    class Meta:
        verbose_name_plural="Dias"
        db_table="dia"

    def __str__(self):
        return self.descripcion

    def delete(self):
        pass

class EstadoClase(models.Model):

    id                  = models.AutoField(primary_key=True)
    descripcion         = models.CharField(blank=False, null=False, max_length=255, unique=True)
    es_activo           = models.BooleanField(default=True)
    es_delete           = models.BooleanField(default=False)
    fecha_crea          = models.DateField(default=timezone.now, help_text=("creation date"))
    fecha_modi          = models.DateField(auto_now=True, null= True)

    class Meta:
        verbose_name_plural="EstadoClases"
        db_table="estado_clase"

    def __str__(self):
        return self.descripcion

    def delete(self):
        pass

class Equipo(models.Model):
    id                  = models.AutoField(primary_key=True)
    descripcion         = models.CharField(blank=False, null=False, max_length=255, unique=True)
    taller              = models.ForeignKey(Taller,null=False, on_delete=models.DO_NOTHING,verbose_name="Taller")
    es_titular          = models.BooleanField(default=True)
    es_interno          = models.BooleanField(default=True)
    es_activo           = models.BooleanField(default=True)
    es_delete           = models.BooleanField(default=False)
    fecha_crea          = models.DateField(default=timezone.now, help_text=("creation date"))
    fecha_modi          = models.DateField(auto_now=True, null= True)

    class Meta:
        verbose_name_plural="Equipos"
        db_table="equipo"

    def __str__(self):
        return self.descripcion

    def delete(self):
        pass

class Gimnacio(models.Model):

    id                  = models.AutoField(primary_key=True)
    descripcion         = models.CharField(blank=False, null=False, max_length=255, unique=True)
    direccion           = models.CharField(blank=False, null=False, max_length=255)
    comuna              = models.ForeignKey(Comuna,null=False, on_delete=models.DO_NOTHING,verbose_name="Comuna")
    fono                = models.CharField(blank=False, null=False, max_length=20)
    email               = models.EmailField(blank=False, null=False, max_length=255)
    numero_canchas      = models.IntegerField(blank=False, null=False)
    es_activo           = models.BooleanField(default=True)
    es_delete           = models.BooleanField(default=False)
    fecha_crea          = models.DateField(default=timezone.now, help_text=("creation date"))
    fecha_modi          = models.DateField(auto_now=True, null= True)

    class Meta:
        verbose_name_plural="Gimnacios"
        db_table="gimnacio"

    def __str__(self):
        return self.descripcion

    def delete(self):
        pass


class Plan(models.Model):

    id                  = models.AutoField(primary_key=True)
    taller              = models.ForeignKey(Taller,null=False, on_delete=models.DO_NOTHING,verbose_name="Taller")
    periodo             = models.ForeignKey(Periodo,null=False, on_delete=models.DO_NOTHING,verbose_name="Periodo")
    valor_matricula     = models.IntegerField(blank=False, null=False)
    valor_clase         = models.IntegerField(blank=False, null=False)
    es_activo           = models.BooleanField(default=True)
    es_delete           = models.BooleanField(default=False)
    fecha_crea          = models.DateField(default=timezone.now, help_text=("creation date"))
    fecha_modi          = models.DateField(auto_now=True, null= True)

    class Meta:
        verbose_name_plural="Planes"
        db_table="plan"

    def __str__(self):
        return self.descripcion

    def delete(self):
        pass


class Persona(models.Model):
    id                      = models.AutoField(primary_key=True)
    dna                     = models.CharField(blank=False, null=False, max_length=25, unique=True,verbose_name="Rut o Dna")
    dv                      = models.CharField(blank=False, null=False, max_length=2,verbose_name="Digito Verificador")
    nombres                 = models.CharField(blank=False, null=False, max_length=100,verbose_name="Nombres")
    apellido_paterno        = models.CharField(blank=False, null=False, max_length=100,verbose_name="Apellido Paterno")
    apellido_materno        = models.CharField(blank=False, null=False, max_length=100,verbose_name="Apellido Materno")
    genero                  = models.ForeignKey(Genero,null=True, on_delete=models.DO_NOTHING,verbose_name="Genero")
    fecha_nacimiento        = models.DateField(blank=False, null=False, verbose_name="Fceha de Nacimiento")
    estado_civil            = models.ForeignKey(EstadoCivil,null=False, on_delete=models.DO_NOTHING,verbose_name="Estado Civil")
    pais_origen             = models.ForeignKey(Pais,null=False, on_delete=models.DO_NOTHING,verbose_name="Nacionalidad")
    sistema_salud           = models.ForeignKey(SistemaSalud,null=False, on_delete=models.DO_NOTHING,verbose_name="Sistema de Salud")
    ocupacion               = models.CharField(blank=False, null=False, max_length=255)
    direccion               = models.CharField(blank=False, null=False, max_length=255)
    comuna                  = models.ForeignKey(Comuna,null=False, on_delete=models.DO_NOTHING,verbose_name="Comuna")
    movil                   = models.CharField(blank=False, null=False, max_length=20)
    fono                    = models.CharField(blank=False, null=False, max_length=20)
    email_personal          = models.EmailField(blank=False, null=False, max_length=255)
    club_origen             = models.ForeignKey(Club,null=False, on_delete=models.DO_NOTHING,verbose_name="Club Origen")
    equipo                  = models.ForeignKey(Equipo,null=False, on_delete=models.DO_NOTHING,verbose_name="Equipo")
    posicion                = models.ForeignKey(Posicion,null=False, on_delete=models.DO_NOTHING,verbose_name="Posicion Estudiante")
    observaciones           = models.TextField(blank=True, null=True)
    es_docente              = models.BooleanField(default=False)
    es_activo               = models.BooleanField(default=True)
    es_delete               = models.BooleanField(default=False)
    fecha_crea              = models.DateField(default=timezone.now, help_text=("creation date"))
    fecha_modi              = models.DateField(auto_now=True, null= True)
    class Meta:
        verbose_name_plural="Personas"
        db_table="persona"

    def __str__(self):
        return "{} {} {} ".format(self.apellido_paterno,self.apellido_materno,self.nombres)

    def delete_logico(self):
        if self.es_delete : return
        self.es_delete=True
        self.save()


class ClaseEnc(models.Model):

    id                  = models.AutoField(primary_key=True)
    fecha               = models.DateField(default=timezone.now, help_text=("Fecha Clase"))
    gimnacio            = models.ForeignKey(Gimnacio,null=False, on_delete=models.DO_NOTHING,verbose_name="Recinto")
    profesor            = models.ForeignKey(Persona,null=False, on_delete=models.DO_NOTHING,verbose_name="Docente")
    estado_clase        = models.ForeignKey(EstadoClase,null=False, on_delete=models.DO_NOTHING,verbose_name="Estado Clase")
    temario             = models.TextField(blank=True, null=True)
    hora_inicio         = models.CharField(max_length=50, default=get_default_my_hour)
    hora_fin            = models.CharField(max_length=50, default=get_default_my_hour)
    numero_asistentes   = models.IntegerField(blank=False, null=False)
    es_activo           = models.BooleanField(default=True)
    es_delete           = models.BooleanField(default=False)
    fecha_crea          = models.DateField(default=timezone.now, help_text=("creation date"))
    fecha_modi          = models.DateField(auto_now=True, null= True)

    class Meta:
        verbose_name_plural="ClaseEncs"
        db_table="clase_enc"

    def __str__(self):
        return self.descripcion

    def delete(self):
        pass
