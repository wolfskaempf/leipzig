from django import forms

from django.forms import ModelForm

from .models import SongWish, Feedback, Comment

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

class CommentForm(ModelForm):
    """ Used to take in comments on articles """
    class Meta:
        model = Comment
        fields = ("name", "text")
