from django.contrib import admin

# Register your models here.
from .models import *



class ArticleAdmin(admin.ModelAdmin):
    """ Used to manage display options in the Django Admin """
    list_display = ("title", "author", "author_country")
    list_filter = ("author",)
    search_fields = ("title", "author", "author_country", "text", "introduction", "pk")

class OfTheDayAdmin(admin.ModelAdmin):
    """ Used to manage of the day objects in the Django admin """
    list_display = ("description", "pk", "image_link")
    search_fields = ("description", "pk", "image_link")


class FeedbackAdmin(admin.ModelAdmin):
    """ Used to manage the feedback from users in the Django Admin """
    list_display = ("name", "text", "committee","team", "timestamp")
    search_fields = ("name", "text", "committee","team", "timestamp")
    list_filter = ("committee","team", "timestamp")


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

class ProgrammeAdmin(admin.ModelAdmin):
    """ Used to manage the programme inside the Django Admin """
    list_display = ("text", "date", "last_updated")
    search_fields = ("text", "date", "last_updated")

class UpdateAdmin(admin.ModelAdmin):
    """ Used to manage the latest updates inside the Django Admin """
    list_display = ("time", "text", "pk")
    search_fields = ("time", "text", "pk")

class ChatMessageAdmin(admin.ModelAdmin):
    """ Used to manage chat messages inside the Django Admin """
    list_display = ("text", "name", "committee",)
    search_fields = ("text", "name", "committee",)

class TopicAdmin(admin.ModelAdmin):
    """ Used to manage topics and rationales inside the Django Admin """
    list_display = ("committee_acronym", "topic",)
    search_fields = ("committee_acronym", "topic",)

class CommentAdmin(admin.ModelAdmin):
    """ Used to manage comments inside the Django Admin """
    list_display = ("article", "name", "text", "timestamp")
    search_fields = ("article", "name", "text", "timestamp")
    list_filter = ("article", "timestamp", "name")


admin.site.register(Article, ArticleAdmin)
admin.site.register(OfTheDay, OfTheDayAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(House, HouseAdmin)
admin.site.register(Song, SongAdmin)
admin.site.register(SongWish, SongWishAdmin)
admin.site.register(Programme, ProgrammeAdmin)
admin.site.register(Update, UpdateAdmin)
admin.site.register(ChatMessage, ChatMessageAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Comment, CommentAdmin)
