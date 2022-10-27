from this import d
from django.shortcuts import render

import datetime as d
# Create your views here.

def index(request):
    now=d.datetime.now()
    return render(request,"newyear/index.html",{
        "newyear": now.month==1 and now.day==1,
        "newyr":True
    })