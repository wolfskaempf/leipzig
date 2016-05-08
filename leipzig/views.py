import datetime
from django.shortcuts import render, render_to_response
from django.contrib import messages


from .models import Update, Programme, FeaturedItem, SongWish, Article, Comment, Link, Feedback, House, Topic, Setting, TeamMember, NavbarEntry
from .forms import SongWishForm, FeedbackForm, CommentForm
# Create your views here.

def home(request):
    """ Serves the homepage """

    view = "home" # This is used to determine whether some buttons should be shown in the latest updates part of the home page

    settings = Setting.objects.last()
    navbar_entries = NavbarEntry.objects.filter(active = True).order_by("order")

    updates = Update.objects.all() # Here we get all updates so we can count them
    update_count = updates.count() # here we assign the total number of updates to the update_count
    updates = updates.order_by("-time")[:2] # here we reduce the number of updates which should be shown to two

    today = datetime.datetime.now().date()

    if Programme.objects.filter(date = today).count() == 1:
        programme = Programme.objects.get(date = today)
    else:
        programme = None

    if Article.objects.filter(published=True):
        articles = Article.objects.filter(published=True).order_by("-published_on")[:9]
    else:
        articles = None

    daily = FeaturedItem.objects.last()

    context = {"updates": updates, "programme": programme, "articles": articles, "daily": daily, "view": view, "update_count": update_count, "settings": settings, "navbar_entries": navbar_entries}

    return render_to_response("home.html", context)

def updates(request):
    """ Serves the latest updates """
    settings = Setting.objects.last()
    navbar_entries = NavbarEntry.objects.filter(active = True).order_by("order")

    updates = Update.objects.all().order_by("-time")
    context = {"updates": updates, "settings": settings, "navbar_entries": navbar_entries}

    return render_to_response("updates.html", context)

def programme(request):
    """ Serves the programme """
    settings = Setting.objects.last()
    navbar_entries = NavbarEntry.objects.filter(active = True).order_by("order")

    programmes = Programme.objects.all().order_by("date")

    context = {"programmes": programmes, "settings": settings, "navbar_entries": navbar_entries}

    return render_to_response("programme.html", context)

def articles(request):
    """ Serves a list of all articles """
    settings = Setting.objects.last()
    navbar_entries = NavbarEntry.objects.filter(active = True).order_by("order")

    articles = Article.objects.filter(published=True).order_by("-published_on")
    context = {"articles": articles, "settings": settings}

    return render_to_response("article_list.html", context)


def article_single(request, pk):
    """ Serves a single article """
    settings = Setting.objects.last()
    navbar_entries = NavbarEntry.objects.filter(active = True).order_by("order")

    form = CommentForm
    article = Article.objects.get(pk=pk)

    if request.method == "POST":
        response = CommentForm(request.POST)
        if response.is_valid():
            response = response.save(commit=False)
            response.article = Article.objects.get(pk=pk)
            response.save()
            messages.add_message(request, messages.SUCCESS, 'Your comment has been saved!')

    context = {"article": article, "form": form, "settings": settings, "navbar_entries": navbar_entries}

    return render(request, "article_single.html", context)


def song_wish(request):
    """ Handles song wishes and provides a form """
    settings = Setting.objects.last()
    navbar_entries = NavbarEntry.objects.filter(active = True).order_by("order")


    form = SongWishForm
    context = {"form": form, "settings": settings, "navbar_entries": navbar_entries}

    if request.method == "POST":
        form = SongWishForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your song wish was added!')

    return render(request, "song_wish.html", context)


def feedback(request):
    """ Handles feedback and provides a form """
    settings = Setting.objects.last()
    navbar_entries = NavbarEntry.objects.filter(active = True).order_by("order")

    form = FeedbackForm
    context = {"form": form, "settings": settings, "navbar_entries": navbar_entries}

    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your feedback has been saved!')

    return render(request, "feedback.html", context)


def houses(request):
    """ Serves a list of all houses and their points """
    settings = Setting.objects.last()
    navbar_entries = NavbarEntry.objects.filter(active = True).order_by("order")

    houses = House.objects.all().order_by("-points")
    context = {"houses": houses, "settings": settings, "navbar_entries": navbar_entries}
    return render_to_response("houses.html", context)

def topics(request):
    """ Serves a list of all topics """
    settings = Setting.objects.last()
    navbar_entries = NavbarEntry.objects.filter(active = True).order_by("order")

    topics = Topic.objects.all().order_by("committee_acronym")
    context = {"topics": topics, "settings": settings, "navbar_entries": navbar_entries}
    return render_to_response("topics.html", context)

def topic_single(request, pk):
    """ Serves a single topic and its rationales """
    settings = Setting.objects.last()
    navbar_entries = NavbarEntry.objects.filter(active = True).order_by("order")

    topic = Topic.objects.get(pk=pk)
    context = {"topic": topic, "settings": settings, "navbar_entries": navbar_entries}
    return render_to_response("topic_single.html", context)

def team(request):
    """ Serves a list of all team members """
    settings = Setting.objects.last()
    navbar_entries = NavbarEntry.objects.filter(active = True).order_by("order")

    team = TeamMember.objects.all().order_by("rank")
    context = {"team": team, "settings": settings, "navbar_entries": navbar_entries}
    return render_to_response("team.html", context)


##### STATIC views

def partners(request):
    """ Shows the static partners.html """
    settings = Setting.objects.last()
    navbar_entries = NavbarEntry.objects.filter(active = True).order_by("order")

    context = {"settings": settings, "navbar_entries": navbar_entries}
    return render_to_response("partners.html", context)

def dictionary(request):
    """ Shows the static dictionary.html """
    settings = Setting.objects.last()
    navbar_entries = NavbarEntry.objects.filter(active = True).order_by("order")

    context = {"settings": settings, "navbar_entries": navbar_entries}
    return render_to_response("dictionary.html", context)

def phones(request):
    """ Shows the static phones.html """
    settings = Setting.objects.last()
    navbar_entries = NavbarEntry.objects.filter(active = True).order_by("order")

    context = {"settings": settings, "navbar_entries": navbar_entries}
    return render_to_response("phones.html", context)

def imprint(request):
    """ Shows the static imprint.html """
    settings = Setting.objects.last()
    navbar_entries = NavbarEntry.objects.filter(active = True).order_by("order")

    context = {"settings": settings, "navbar_entries": navbar_entries}
    return render_to_response("imprint.html", context)

def datenschutzerklaerung(request):
    """ Shows the static datenschutzerklaerung.html """
    settings = Setting.objects.last()
    navbar_entries = NavbarEntry.objects.filter(active = True).order_by("order")

    context = {"settings": settings, "navbar_entries": navbar_entries}
    return render_to_response("datenschutzerklaerung.html", context)
