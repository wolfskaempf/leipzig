import datetime
from django.shortcuts import render, render_to_response
from django.contrib import messages


from .models import *
from .forms import *
# Create your views here.
def home(request):
    """ Serves the homepage """

    updates = Update.objects.all().order_by("-time")

    today = datetime.datetime.now().day

    if Programme.objects.filter(date__day = today).count() == 1:
        programme = Programme.objects.get(date__day = today)
    else:
        programme = None

    if Article.objects.filter(published=True):
        articles = Article.objects.filter(published=True).order_by("-published_on")[:3]
    else:
        articles = None

    daily = OfTheDay.objects.last()

    context = {"updates": updates, "programme": programme, "articles": articles, "daily": daily}

    return render_to_response("home.html", context)

def programme(request):
    """ Serves the programme """
    programmes = Programme.objects.all().order_by("date")

    context = {"programmes": programmes}

    return render_to_response("programme.html", context)

def articles(request):
    """ Serves a list of all articles """
    articles = Article.objects.filter(published=True).order_by("-published_on")
    context = {"articles": articles}

    return render_to_response("article_list.html", context)


def article_single(request, pk):
    """ Serves a single article """
    form = CommentForm
    article = Article.objects.get(pk=pk)

    if request.method == "POST":
        response = CommentForm(request.POST)
        if response.is_valid():
            response = response.save(commit=False)
            response.article = Article.objects.get(pk=pk)
            response.save()
            messages.add_message(request, messages.SUCCESS, 'Your comment has been saved!')

    context = {"article": article, "form": form}

    return render(request, "article_single.html", context)


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
            messages.add_message(request, messages.SUCCESS, 'Your feedback has been saved!')

    return render(request, "feedback.html", context)


def houses(request):
    """ Serves a list of all houses and their points """
    houses = House.objects.all().order_by("-points")
    context = {"houses": houses}
    return render_to_response("houses.html", context)

def topics(request):
    """ Serves a list of all topics """
    topics = Topic.objects.all().order_by("committee_acronym")
    context = {"topics": topics}
    return render_to_response("topics.html", context)

def topic_single(request, pk):
    """ Serves a single topic and its rationales """
    topic = Topic.objects.get(pk=pk)
    context = {"topic": topic}
    return render_to_response("topic_single.html", context)


##### STATIC views

def partners(request):
    """ Shows the static partners.html """
    return render_to_response("partners.html")

def dictionary(request):
    """ Shows the static dictionary.html """
    return render_to_response("dictionary.html")

def phones(request):
    """ Shows the static phones.html """
    return render_to_response("phones.html")

def imprint(request):
    """ Shows the static imprint.html """
    return render_to_response("imprint.html")

def datenschutzerklaerung(request):
    """ Shows the static datenschutzerklaerung.html """
    return render_to_response("datenschutzerklaerung.html")
