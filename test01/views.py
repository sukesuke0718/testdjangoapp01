from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def index(request):
    text_sample_lists = ['Love Live!',
                        'スバラシイコエノヒト'
    ]
    context = {'text_sample_lists': text_sample_lists}
    return render(request, 'test01/index.html', context)