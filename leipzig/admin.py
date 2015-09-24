from django.contrib import admin

# Register your models here.
from .models import *



class ArticleAdmin(admin.ModelAdmin):
    """ Used to manage display options in the Django Admin """
    list_display = ("title", "author", "author_country")
    list_filter = ("author",)
    search_fields = ("title", "author", "author_country", "text", "introduction", "pk")

class PhotoAdmin(admin.ModelAdmin):
    """ Used to manage photos in the Django admin """
    list_display = ("description", "pk", "link")
    search_fields = ("description", "pk", "link")


class FeedbackAdmin(admin.ModelAdmin):
    """ Used to manage the feedback from users in the Django Admin """
    list_display = ("name", "text")
    search_fields = ("name", "text")

class HouseAdmin(admin.ModelAdmin):
    """ Used to manage the points of houses in the Django Admin """
    list_display = ("name", "points")
    search_fields = ("name", "points")

class SongAdmin(admin.ModelAdmin):
    """ Used to manage the songs in the Django Admin """
    list_display = ("title", "artist",)
    search_fields = ("title", "artist",)

class SongWishAdmin(admin.ModelAdmin):
    """ Used to manage the song wishes in the Django Admin """
    list_display = ("title", "artist",)
    search_fields = ("title", "artist",)
    # verbose_name_plural = "SongWishes"
