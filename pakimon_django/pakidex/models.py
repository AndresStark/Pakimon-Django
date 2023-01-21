from django.db import models


class PakimonData(models.Model):
    name = models.CharField(max_length=100, default=None)
    life = models.IntegerField(default=0)
    attack = models.IntegerField(default=0)
    img = models.CharField(max_length=100, default=None)

    def __str__(self):
        return str(self.pk)