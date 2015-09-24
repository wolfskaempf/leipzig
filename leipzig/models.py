from django.db import models

# Create your models here.
class Update(models.Model):
    """Used to store updates to be shown to users"""
    text = models.TextField()

class Programme(models.Model):
    """Used to store the programme for a specific date"""
    text = models.TextField()
    last_updated = DateTimeField(auto_now = True,)
    date = DateField(auto_now = False,)
