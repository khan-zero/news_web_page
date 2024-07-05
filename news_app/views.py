#from django.shortcuts import render
from . import models
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def index(request):
    nimadur = models.News.objects.all()
    context = {
        'posts': nimadur
    }
    
    template = loader.get_template('index.html')
    
    return HttpResponse(template.render({}, request))
