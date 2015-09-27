import datetime
from django.utils import timezone
from django.db import models

# Create your models here.
class Update(models.Model):
    """Used to store updates to be shown to users"""
    time = models.DateTimeField(auto_now = True,)
    text = models.TextField()

class Programme(models.Model):
    """Used to store the programme for a specific date"""
    text = models.TextField()
    last_updated = models.DateTimeField(auto_now = True,)
    date = models.DateField(auto_now = False,)

class Photo(models.Model):
    """Used to store information about a photo"""
    link = models.URLField()
    description = models.CharField(max_length = 200, blank = True,)

class Song(models.Model):
    """Used to store information on the karaoke lyrics"""
    title = models.CharField(max_length = 40,)
    artist = models.CharField(max_length = 40,)
    lyrics = models.TextField()
    video_link = models.URLField(blank = True, null = True,)
    spotify_link = models.URLField(blank = True, null = True,)

class SongWish(models.Model):
    """Used to store the song wishes"""
    title = models.CharField(max_length = 40, )
    artist = models.CharField(max_length = 40, )
    video_link = models.URLField(blank = True, null = True)
    spotify_link = models.URLField(blank = True, null = True)

class ChatMessage(models.Model):
    """Used to store all chat messages of the session chat"""
    name = models.CharField(max_length = 50, )
    committee = models.CharField(max_length = 10, blank = True,)
    text = models.TextField()

class Article(models.Model):
    """Used to store articles """
    title = models.CharField(max_length = 100, )
    author = models.CharField(max_length = 100, )
    author_country = models.CharField(max_length = 100, )
    published_on = models.DateTimeField(auto_now = False)
    text = models.TextField()
    introduction = models.TextField(blank = True,)
    external_link = models.URLField(blank = True, null = True)
    image_link = models.URLField(blank = True, null = True)
    video_embed_code = models.TextField(blank = True, )

class Feedback(models.Model):
    """Used to store feedback from users"""
    name = models.CharField(max_length = 50, blank = True, )
    text = models.TextField()

class House(models.Model):
    """Used to store houses and corresponding points"""
    name = models.CharField(max_length = 100,)
    points = models.IntegerField()
