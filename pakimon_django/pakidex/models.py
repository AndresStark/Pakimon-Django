from django.db import models


class Pakimon(models.Model):
    name = models.CharField(max_length=100, default=None)