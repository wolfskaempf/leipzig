from django.contrib import admin

# Register your models here.
from .models import Update, Programme, FeaturedItem, SongWish, Article, Comment, Link, Feedback, House, Topic, Setting, TeamMember


class LinkAdmin(admin.ModelAdmin):
    """ Used to manage links inside the Django Admin """
    list_display = ("article", "button_text", "link")
    search_fields = ("article", "button_text", "link")
    list_filter = ("article", "link")

class LinkInline(admin.TabularInline):
    """ This allows the article admin to display link edit forms directly inside the article """
    model = Link

class ArticleAdmin(admin.ModelAdmin):
    """ Used to manage display options in the Django Admin """
    list_display = ("title", "author", "author_country", "published")
    list_filter = ("author","published")
    search_fields = ("title", "author", "author_country", "text", "introduction", "pk")
    inlines = [LinkInline]

class FeaturedItemAdmin(admin.ModelAdmin):
    """ Used to manage featured objects in the Django admin """
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

class SongWishAdmin(admin.ModelAdmin):
    """ Used to manage the song wishes in the Django Admin """
    list_display = ("title", "artist",)
    search_fields = ("title", "artist",)
    # verbose_name_plural = "SongWishes"

class ProgrammeAdmin(admin.ModelAdmin):
    """ Used to manage the programme inside the Django Admin """
    list_display = ("text", "date", "last_updated")
    search_fields = ("text", "date", "last_updated")
    ordering = ["date"]

class UpdateAdmin(admin.ModelAdmin):
    """ Used to manage the latest updates inside the Django Admin """
    list_display = ("time", "text", "pk")
    search_fields = ("time", "text", "pk")

class TopicAdmin(admin.ModelAdmin):
    """ Used to manage topics and rationales inside the Django Admin """
    list_display = ("committee_acronym", "topic",)
    search_fields = ("committee_acronym", "topic",)

class TeamMemberAdmin(admin.ModelAdmin):
    """ Used to manage team members inside the Django Admin """
    list_display = ("name", "rank", "role")
    search_fields = ("name", "rank", "role")

class CommentAdmin(admin.ModelAdmin):
    """ Used to manage comments inside the Django Admin """
    list_display = ("article", "name", "text", "timestamp")
    search_fields = ("article", "name", "text", "timestamp")
    list_filter = ("article", "timestamp", "name")

class SettingAdmin(admin.ModelAdmin):
    """ Used to manage Settings inside the Django Admin """
    list_display = ("app_title", "app_colour")
    search_fields = ("app_title", "app_colour")
    list_filter = ("app_title", "app_colour")



admin.site.register(Article, ArticleAdmin)
admin.site.register(FeaturedItem, FeaturedItemAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(House, HouseAdmin)
admin.site.register(SongWish, SongWishAdmin)
admin.site.register(Programme, ProgrammeAdmin)
admin.site.register(Update, UpdateAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(TeamMember, TeamMemberAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(Setting, SettingAdmin)
