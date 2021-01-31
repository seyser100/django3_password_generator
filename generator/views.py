from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    
    thepassword = ""
    
    characters_lower = list('abcdefghijklmnopqrstuvwxyz')
    
    lenght = int(request.GET.get('length',8))
    is_uppercase = request.GET.get('uppercase')
    is_numbers = request.GET.get('number')
    is_special = request.GET.get('special')
    
    if is_uppercase:
        characters_lower.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if is_numbers:
        characters_lower.extend('1234567890')
    if is_special:
        characters_lower.extend('!@#$%^&*()')
    
    for x in range(lenght):
        thepassword += random.choice(characters_lower)
        
    return render(request, 'generator/password.html', {'password':thepassword})


def about(request):
    return render(request, 'generator/about.html')