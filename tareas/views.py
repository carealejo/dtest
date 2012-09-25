from django.views.generic import *

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
