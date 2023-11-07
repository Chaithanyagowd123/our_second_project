from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def varma(request):
    return HttpResponse("<marquee><h1>worth varma worthu....<h1></marquee>")