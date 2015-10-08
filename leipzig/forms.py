from django import forms

from django.forms import ModelForm

from .models import SongWish, Feedback

class SongWishForm(ModelForm):
    """ Used to generate a form for song wishes """
    class Meta:
        model = SongWish
        fields = "__all__"


class FeedbackForm(ModelForm):
    """ Used to generate a form for giving feedback """
    class Meta:
        model = Feedback
        fields = "__all__"
