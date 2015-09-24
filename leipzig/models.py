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

class Photo(models.Model):
    """Used to store information about a photo"""
    link = URLField()
    description = CharField(max_length = 200,)

class Song(models.Model):
    """Used to store information on the karaoke lyrics"""
    title = CharField(max_length = 40, required = True,)
    artist = CharField(max_length = 40, required = True,)
    lyrics = TextField(required = True,)
    video_link = URLField(null = True, required = False,)
    spotify_link = URLField(null = True, required = False,)

class SongWish(models.Model):
    """Used to store the song wishes"""
    title = CharField(max_length = 40, required = True,)
    artist = CharField(max_length = 40, required = True,)
    video_link = URLField(null = True, required = False,)
    spotify_link = URLField(null = True, required = False,)
