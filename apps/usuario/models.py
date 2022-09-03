from distutils.command.upload import upload
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Usuario(AbstractUser):
    
    imagen = models.FileField(null=True, blank=True , upload_to = "Uploaded Files/")

    def get_absolute_url(self):
        return reverse('index')