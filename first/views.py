from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Hello Django World")

def welcoming(request):
    return HttpResponse("Welcome dear user!!!")