
from django.db import models

# Create your models here.
class Carrousel(models.Model):
    imagen = models.FileField(null=True, blank=True , upload_to = "Uploaded Files/")
    title = models.CharField(max_length=150, default="titulo")

    def __str__(self):
        return self.title