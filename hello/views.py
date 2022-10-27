from nturl2path import url2pathname
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django import forms

from hello import urls

class NameForm(forms.Form):
    name=forms.CharField(label="Enter your name")
def index(request):
    if request.method=="POST":
        form=NameForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data["name"]
            return HttpResponseRedirect(f"/hello/{name}")
    return render(request,"hello/index.html",{
        "form":NameForm(),
        "hello":True
    })

def greet(request,name):
    return render(request, "hello/greet.html",{
        "name": name.capitalize()
    })