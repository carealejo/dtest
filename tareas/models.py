# -*- coding: utf-8 -*- 

from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.core.urlresolvers import reverse
from django import forms

Estado_Tareas = (
    ('Finalizada', 'Finalizada'),
    ('En proceso', 'En proceso'),
    ('No iniciada', 'No iniciada'),
    )

class Tarea(models.Model):
    nombre = models.CharField(max_length=200)
    fechaini = models.DateTimeField('Fecha de inicio')
    fechafin = models.DateTimeField('Fecha de finalización')
    descripcion = models.CharField(max_length=500)
    estado = models.CharField(max_length=11,
                              choices=Estado_Tareas)
    usuario = models.ForeignKey(User)

    def get_absolute_url(self):
        return reverse('tarea_detail', args=[self.pk])
    
    def __unicode__(self):
        return self.nombre

class TareaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Tarea, TareaAdmin)
