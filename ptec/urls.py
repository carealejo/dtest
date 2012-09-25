from django.conf.urls import patterns, include, url
from django.views.generic import *
from tareas.models import Tarea

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       (r'^tareas/$', ListView.as_view(
            model=Tarea,
            )),
                       (r'^tareas/detalle/(?P<pk>\d+)/$', DetailView.as_view(
            model=Tarea,
            )),
                       (r'^tareas/crear/$', CreateView.as_view(
            model=Tarea,
            )),
                       
                       
                       (r'^tareas/crear/?$', 
                        'django.views.generic.create_update.create_object',
                        dict(model=Tarea,post_save_redirect="/tareas/") ),
                       
                       )

# urlpatterns += patterns('',
#                         url (
#         regex = '^list/$',
#         view =  TareaListView.as_view(),
#         name = 'tarea_list'
#         ),
                        
#                         url (
#         regex = '^detail/(?P\d+)/$',
#         view =  TareaDetailView.as_view(),
#         name = 'tarea_detail'
#         ),
#                         url (
#         regex = '^create/$',
#         view =  TareaCreateView.as_view(),
#         name = 'tarea_create'
#         ),
                        
#                         url (
#         regex = '^delete/(?P\d+)/$',
#         view =  TareaDeleteView.as_view(),
#         name = 'tarea_delete'
#         ),
#                         url (
#         regex = '^update/(?P\d+)/$',
#         view =  TareaUpdateView.as_view(),
#         name = 'tarea_update'
#         ),
#                         )
