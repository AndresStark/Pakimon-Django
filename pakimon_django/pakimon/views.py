from django.shortcuts import render
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'pakimon/index.html'
    context_object_name = 'pakimon'

    def get_queryset(self):
        pass
