from django.shortcuts import render
import datetime as d
# Create your views here.

def index(request):
    now=d.datetime.now()
    return render(request,"birthday/index.html",{
        "birthday": now.month==10 and now.day==22,
        "bday":True
    })