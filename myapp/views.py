from django.shortcuts import render

from django.http import HttpResponse

from .models import Verification

def home_view(request):
    return render(request, "home.html")

# def index(request):
#     return HttpResponse("hello w0rld")