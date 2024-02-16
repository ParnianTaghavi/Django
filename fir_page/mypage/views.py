from django.shortcuts import render
from django.http import HttpResponse

def mainpage (request) :
    return HttpResponse("My First Page")
# Create your views here.
