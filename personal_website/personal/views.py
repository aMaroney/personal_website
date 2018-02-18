from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.base import *

def index(request):
    return render(request, 'personal/home.html')

def contact(request):
    return render(request, 'personal/basic.html', {'content':['If you would like to contact me, my email address is AMaroney92@gmail.com'
                                                              '','']})

def weather(request):
    pull_weather_file = HttpResponse(open('weather_for_website.txt').read(), content_type='text/plain; utf-8')
    return pull_weather_file