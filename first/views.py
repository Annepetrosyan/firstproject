from django.shortcuts import render, HttpResponse
import datetime
from datetime import datetime

# Create your views here.

def home(request):
    return HttpResponse("Hello Django World")

def welcoming(request):
    return HttpResponse("Welcome dear user!!!")

def introduce(request):
    return HttpResponse("Website is created for You to make your daily 'To do' list")

def datetime_(request):
    now = datetime.now()
    return HttpResponse(f"Current date and time = {now}")



