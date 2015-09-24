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

class ChatMessage(models.Model):
    """Used to store all chat messages of the session chat"""
    name = CharField(max_length = 50,)
    committee = CharField(max_length = 10,)
    text = TextField()

class Article(models.Model):
    """Used to store articles """
    title = CharField(max_length = 40, required = True,)
    author = CharField(max_length = 40, required = True,)
    author_country = CharField(max_length = 100, required = True,)
    text = TextField(required = True,)
    introduction = TextField(required = False, null = True,)
    media_link = URLField(null = True, required = False,)
    image_link = URLField(null = True, required = False,)
    video_embed_code = TextField(null = true, required = False)
