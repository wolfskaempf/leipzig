from django.contrib import admin

# Register your models here.
from .models import *



class ArticleAdmin(admin.ModelAdmin):
    """ Used to manage display options in the Django Admin """
    list_display = ("title", "author", "author_country")
    list_filter = ("author",)
    search_fields = ("title", "author", "author_country", "text", "introduction", "pk")
