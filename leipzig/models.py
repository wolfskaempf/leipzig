from django.db import models

# Create your models here.
class Update(models.Model):
    """Used to store updates to be shown to users"""
    text = models.TextField()
