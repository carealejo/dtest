from django.conf.urls import patterns, include, url
from django.views.generic import *
from tareas.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url (
        regex = '^list/$',
        view =  TareaListView.as_view(),
        name = 'tarea_list'
        ),
                        
                        url (
        regex = '^detail/(?P<pk>\d+)/$',
        view =  TareaDetailView.as_view(),
        name = 'tarea_detail'
        ),
                        url (
        regex = '^create/$',
        view =  TareaCreateView.as_view(),
        name = 'tarea_create'
        ),
                        
                        url (
        regex = '^delete/(?P<pk>\d+)/$',
        view =  TareaDeleteView.as_view(),
        name = 'tarea_delete'
        ),
                        url (
        regex = '^update/(?P<pk>\d+)/$',
        view =  TareaUpdateView.as_view(),
        name = 'tarea_update'
        ),
                        )
