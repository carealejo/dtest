from django.views.generic import *
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from tareas.models import Tarea

class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)

class TareaMixin(LoginRequiredMixin):
    model = Tarea

    def get_success_url(self):
        return reverse('tarea_list')

class TareaListView(TareaMixin, ListView):
    pass
class TareaDetailView(TareaMixin, DetailView):
    pass
class TareaCreateView(TareaMixin, CreateView):
    pass
class TareaDeleteView(TareaMixin, DeleteView):
    pass
class TareaUpdateView(TareaMixin, UpdateView):
    pass
