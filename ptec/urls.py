from django.conf.urls import patterns, include, url
from django.views.generic import list_detail
from tareas.models import Tarea

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

tarea_info = {
    'queryset': Tarea.objects.all(),
    }

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       (r'^tareas/$', list_detail.object_list, tarea_info),
                       (r'^tareas/crear/?$', 
                        'django.views.generic.create_update.create_object',
                        dict(model=Tarea,post_save_redirect="/tareas/") ),
                       
                       )
