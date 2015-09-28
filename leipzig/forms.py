from django import forms

from django.forms import ModelForm

from .models import SongWish

class SongWishForm(ModelForm):
    """ Used to generate a form for song wishes """
    class Meta:
        model = SongWish
        fields = "__all__"
