# -*- coding: utf-8 -*-
# Create your views here.
from django.shortcuts import render
from django.http import Http404
import datetime
import os

def home(request):
    context = {'ts' : datetime.datetime.now}
    return render(request, 'home.html', context)

def listing(request, dir_name = ''):
    dir_content = {}
    if os.path.exists(os.path.dirname(os.path.realpath(__file__))+'/var/log/'+dir_name):
        files = os.listdir(os.path.dirname(os.path.realpath(__file__))+'/var/log/'+dir_name)
        for f in files:
            if os.path.isdir(os.path.dirname(os.path.realpath(__file__))+'/var/log/'+dir_name+'/'+f):
                dir_content.update({f: {'link': f, 'size': os.path.getsize(os.path.dirname(os.path.realpath(__file__))+'/var/log/'+dir_name+'/'+f), 'date': datetime.datetime.fromtimestamp(os.path.getmtime(os.path.dirname(os.path.realpath(__file__))+'/var/log/'+dir_name+'/'+f)) }})
            else:
                dir_content.update({f: {'size': os.path.getsize(os.path.dirname(os.path.realpath(__file__))+'/var/log/'+dir_name+'/'+f), 'date': datetime.datetime.fromtimestamp(os.path.getmtime(os.path.dirname(os.path.realpath(__file__))+'/var/log/'+dir_name+'/'+f)) }})
        context = {'dir_content' : dir_content, 'dir_name': '/var/log/'+dir_name}
    else:
        raise Http404
    return render(request, 'listing.html', context)