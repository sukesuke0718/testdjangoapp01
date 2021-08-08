from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def index(request):
    text_sample = 'Love Live!'
    context = {'text_sample': text_sample}
    return render(request, 'test01/index.html', context)