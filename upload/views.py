from django.http import HttpResponse
from django.shortcuts import render, redirect

def upload(request):
    return HttpResponse("You're at the upload index.")

def home(request):
    return render(request, 'home.html',
    {'home': home})