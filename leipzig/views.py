import datetime
from django.shortcuts import render, render_to_response

from .models import *
# Create your views here.
def home(request):
    """ Serves the homepage """

    updates = Update.objects.all()

    context = {"updates": updates}

    return render_to_response("home.html", context)

def programme(request):
    """ Serves the programme """
    programmes = Programme.objects.all().order_by("date")

    context = {"programmes": programmes}

    return render_to_response("programme.html", context)
