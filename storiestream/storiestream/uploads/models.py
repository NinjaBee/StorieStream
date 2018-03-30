from django.db import models
import os
from django.conf import settings

# Create your models here.



class SavedFile(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='files/')

    def __str__(self):
        return self.name
