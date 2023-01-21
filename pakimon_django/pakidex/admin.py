from django.contrib import admin
from .models import PakimonData

class PakimonDataAdmin(admin.ModelAdmin):
    fields = ["name", "life", "attack", "img"]

admin.site.register(PakimonData, PakimonDataAdmin)
