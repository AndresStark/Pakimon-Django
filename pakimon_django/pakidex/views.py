from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

from .forms import PakidexForm
from .models import PakimonData



class IndexView(generic.ListView):
    template_name = 'pakidex/index.html'
    context_object_name = 'pakidex'

    def get_queryset(self):
        return PakimonData.objects.all()

    
class EntryView(generic.ListView):
    model = PakimonData
    template_name = 'pakidex/entry.html'
    form_class = PakidexForm

    def post(self, request):
        if request.method == 'POST':
            form = self.form_class(request.POST)      
            if form.is_valid():
                pakimon = PakimonData.objects.get(pk=int(form.cleaned_data['pakimon_id']))
                return render(request, 'pakidex/entry.html', {'pakimon': pakimon})
        else:
            form = self.form_class()

        pakimon = PakimonData.objects.get(pk=int(form.cleaned_data['pakimon_id']))
        return render(request, 'pakidex/entry.html', {'pakimon': pakimon})

    def get(self, request):
        if request.method == 'GET':
            form = self.form_class(request.GET)
            if form.is_valid():
                pakimon = PakimonData.objects.get(pk=int(form.cleaned_data['pakimon_id']))
                return render(request, 'pakidex/entry.html', {'pakimon': pakimon})
        else:
            form = self.form_class()

        pakimon = PakimonData.objects.get(pk=int(form.cleaned_data['pakimon_id']))
        return render(request, 'pakidex/entry.html', {'pakimon': pakimon})

