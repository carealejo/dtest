# -*- coding: utf-8 -*- 

from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

Estado_Tareas = (
    ('Fin', 'Finalizada'),
    ('Proc', 'En proceso'),
    ('Nini', 'No iniciada'),
    )

class Tarea(models.Model):
    nombre = models.CharField(max_length=200)
    fechaini = models.DateTimeField('Fecha de inicio')
    fechafin = models.DateTimeField('Fecha de finalización')
    descripcion = models.CharField(max_length=500)
    estado = models.CharField(max_length=4,choices=Estado_Tareas)
    usuario = models.ForeignKey(User)

    def get_absolute_url(self):
        return '/tareas/detalle/'+str(self.pk)
    
    def __unicode__(self):
        return self.nombre

class TareaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Tarea, TareaAdmin)
    
