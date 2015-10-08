import datetime
from django.shortcuts import render, render_to_response
from django.contrib import messages


from .models import *
from .forms import *
# Create your views here.
def home(request):
    """ Serves the homepage """

    updates = Update.objects.all()

    today = datetime.datetime.now().day

    if Programme.objects.filter(date__day = today).count() == 1:
        programme = Programme.objects.get(date__day = today)
    else:
        programme = None

    if Article.objects.all():
        articles = Article.objects.all().order_by("-published_on")[:3]
    else:
        articles = None

    photo = Photo.objects.last()

    context = {"updates": updates, "programme": programme, "articles": articles, "photo": photo}

    return render_to_response("home.html", context)

def programme(request):
    """ Serves the programme """
    programmes = Programme.objects.all().order_by("date")

    context = {"programmes": programmes}

    return render_to_response("programme.html", context)

def articles(request):
    """ Serves a list of all articles """
    articles = Article.objects.all().order_by("-published_on")
    context = {"articles": articles}

    return render_to_response("article_list.html", context)


def article_single(request, pk):
    """ Serves a single article """
    article = Article.objects.get(pk=pk)
    context = {"article": article}

    return render_to_response("article_single.html", context)


def song_wish(request):
    """ Handles song wishes and provides a form """
    form = SongWishForm

    context = {"form": form}

    if request.method == "POST":
        form = SongWishForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your song wish was added!')

    return render(request, "song_wish.html", context)


def feedback(request):
    """ Handles feedback and provides a form """
    form = FeedbackForm

    context = {"form": form}

    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your feedback has been sent to the organisers!')

    return render(request, "feedback.html", context)



##### STATIC views

def supporters(request):
    """ Shows the static supporters.html """
    return render_to_response("supporters.html")

def dictionary(request):
    """ Shows the static dictionary.html """
    return render_to_response("dictionary.html")
