from django.shortcuts import render
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'pakidex/index.html'
    context_object_name = 'pakidex'

    def get_queryset(self):
        pass
