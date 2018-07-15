# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts

# Create your views here.


def index(request):

 posts = Posts.objects.all()[:10]
     
 return render(request,'posts/index.html')
