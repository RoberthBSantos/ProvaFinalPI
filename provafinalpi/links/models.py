from django.db import models

# Create your models here.
class Link(models.Model):
    original = models.CharField(max_length=500)
    encurtado = models.CharField(max_length=20)

    def encurtar(self,original, encurtado):
        link = Link(original=original, encurtado=encurtado)
        link.save()

