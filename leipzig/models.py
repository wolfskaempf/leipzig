import datetime
from django.utils import timezone
from django.db import models

# Create your models here.
class Update(models.Model):
    """Used to store updates to be shown to users"""
    time = models.DateTimeField(auto_now = True)
    text = models.TextField()

    def __unicode__(self):
        return u'{0}, {1}'.format(self.text, self.time)

class Programme(models.Model):
    """Used to store the programme for a specific date"""
    text = models.TextField()
    last_updated = models.DateTimeField(auto_now = True)
    date = models.DateField(auto_now = False)

    def __unicode__(self):
        return self.date

class FeaturedItem(models.Model):
    """Used to store information about a of the day object"""
    object_type = models.CharField(max_length = 10, default = "Photo")
    external_link = models.URLField(blank = True)
    image_link = models.URLField()
    description = models.CharField(max_length = 200, blank = True)

    def __unicode__(self):
        return u'{0}, {1}'.format(self.object_type, self.description)

class SongWish(models.Model):
    """Used to store the song wishes"""
    title = models.CharField(max_length = 40)
    artist = models.CharField(max_length = 40)
    video_link = models.URLField(blank = True)
    spotify_link = models.URLField(blank = True)

    def __unicode__(self):
        return u'{0} by {1}'.format(self.title, self.artist)


class Article(models.Model):
    """Used to store articles """
    title = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100)
    author_country = models.CharField(max_length = 100)
    published_on = models.DateTimeField(auto_now = False)
    published = models.BooleanField(default = True)
    introduction = models.TextField()
    text = models.TextField()
    external_link = models.URLField(blank = True)
    image_link = models.URLField(blank = True)
    video_embed_src = models.TextField(blank = True)
    committee_tag = models.CharField(blank = True, max_length = 10)

    def __unicode__(self):
        return u'{0} by {1}'.format(self.title, self.author)

class Comment(models.Model):
    """Used to store comments on articles"""
    article = models.ForeignKey("Article")
    name = models.CharField(max_length = 100,)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now = True,)

    def __unicode__(self):
        return u'{0} says {1}'.format(self.name, self.text)

class Link(models.Model):
    """Used to store links which relate to articles"""
    article = models.ForeignKey("Article")
    button_text = models.CharField(max_length = 100)
    link = models.URLField()

    def __unicode__(self):
        return u'{0} linking to {1}'.format(self.button_text, self.link)

class Feedback(models.Model):
    """Used to store feedback from users"""

    team_choices = (
        ('OT', 'Organising Team'),
        ('MT', 'Media Team'),
    )

    team = models.CharField(max_length=2, choices = team_choices)
    name = models.CharField(max_length = 50, blank = True)
    committee = models.CharField(max_length = 10, blank = True)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now = True,)

    def __unicode__(self):
        return u'{0} says {1}'.format(self.name, self.text)

class House(models.Model):
    """Used to store houses and corresponding points"""
    name = models.CharField(max_length = 100,)
    image_link = models.URLField(blank = True)
    points = models.IntegerField()
    quote = models.TextField(blank = True)
    cite = models.CharField(max_length = 100, blank = True)
    description = models.TextField(blank = True)

    def __unicode__(self):
        return u'{0}, {1} points'.format(self.name, self.points)

class Topic(models.Model):
    """Used to store topics and corresponding reationales"""
    committee_name = models.CharField(max_length = 100)
    committee_acronym = models.CharField(max_length = 10)
    topic = models.TextField()
    image_link = models.URLField(blank = True)
    video_embed_src = models.TextField(blank = True)
    rationale = models.TextField()

    def __unicode__(self):
        return self.committee_acronym

class TeamMember(models.Model):
    """Used to store team members"""
    name = models.CharField(max_length = 100)
    role = models.CharField(max_length = 100)
    tagline = models.TextField(blank = True)
    rank = models.IntegerField(blank = True)
    image_link = models.URLField()

    def __unicode__(self):
        return u'{0}, {1}'.format(self.name, self.role)


class Setting(models.Model):
    """ Used to store general settings like name of the website and colour """
    app_title = models.CharField(max_length = 25, default = "Leipzig 2015")
    app_colour = models.CharField(max_length = 50, default = "purple")
    app_meta_description = models.TextField(blank = True)
    app_analytics = models.TextField(blank = True)
    app_chrome_navbarcolour = models.CharField(max_length = 10, blank = True)


    def __unicode__(self):
        return u'{0}, {1}'.format(self.app_title, self.app_colour)

class Navbar(models.Model):
    """ Used to display navbar entries """
    name = models.CharField(max_length=20)
    link = models.URLField()
    active = models.BooleanField(default = True)
