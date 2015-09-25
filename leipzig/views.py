from django.shortcuts import render, render_to_response

from .models import *
# Create your views here.
def home(request):
    """ Serves the homepage """

    updates = Update.objects.all()

    context = {"updates": updates}

    return render_to_response("home.html", context)

