import datetime
from django.shortcuts import render, render_to_response

from .models import *
# Create your views here.
def home(request):
    """ Serves the homepage """

    updates = Update.objects.all()

    today = datetime.datetime.now().day

    if Programme.objects.filter(date__day = today).count() == 1:
        programme = Programme.objects.get(date__day = today)
    else:
        programme = None

    context = {"updates": updates, "programme": programme}

    return render_to_response("home.html", context)

def programme(request):
    """ Serves the programme """
    programmes = Programme.objects.all().order_by("date")

    context = {"programmes": programmes}

    return render_to_response("programme.html", context)

def articles(request):
    """ Serves a list of recent articles """
    articles = Article.objects.all().order_by("-published_on")
    context = {"articles": articles}

    return render_to_response("articles.html", context)
