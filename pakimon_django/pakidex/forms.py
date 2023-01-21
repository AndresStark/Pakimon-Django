from django import forms
from django.db import models

class PakidexForm(forms.Form):
    pakimon_name = forms.CharField()
    pakimon_id = forms.IntegerField()

    def __str__(self):
        return str(self.pakimon_name)