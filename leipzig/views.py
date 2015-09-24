from django.shortcuts import render, render_to_response

# Create your views here.
def home(request):
    """ Serves the homepage """
    return render_to_response("home.html")
