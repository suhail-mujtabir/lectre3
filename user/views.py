from xml.dom import ValidationErr
from django.http import HttpResponse
# from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django import forms
# from django.http import HttpResponseRedirect
# from django.urls import reverse
from user.models import users
# Create your views here.

class loginform(forms.Form):
    uname=forms.CharField(max_length=10,label="Username")
    password=forms.CharField(widget=forms.PasswordInput(), max_length=64,min_length=8,label="Password")

class newloginform(forms.Form):
    uname=forms.CharField(max_length=10,label="Username")
    password=forms.CharField(widget=forms.PasswordInput(), max_length=64,min_length=8,label="New Password")
    re_pass=forms.CharField(widget=forms.PasswordInput(),max_length=64,min_length=8,label="Re-type New Password")

    # def clean(self):
    #     cleaned_data = super().clean()
    #     password = cleaned_data["password"]
    #     re_pass = cleaned_data["re_pass"]

    #     if password != re_pass:
    #         raise forms.ValidationError('Password do not match')

def login(request):
    if request.method=="POST":
        form=loginform(request.POST)
        if form.is_valid():
            username=form.cleaned_data["uname"]
            password=form.cleaned_data["password"]
            usr=users.objects.filter(uname=username,password=password).values()
            if usr.exists():
                return HttpResponse("Login Success!!")
            else:
                return render(request,"user/index.html",{
                    "msg":"Invalid Username or Password",
                    "form":loginform()
                })
    return render (request,"user/index.html",{
        "form":loginform(),
        "login":True
    })

def newlogin(request):
    if request.method=="POST":
        form=newloginform(request.POST)
        if form.is_valid():
            uname= form.cleaned_data["uname"]
            password = form.cleaned_data["password"]
            re_pass = form.cleaned_data["re_pass"]
            if users.objects.values_list('uname').filter(uname=uname).exists():
                return render(request,"user/newlogin.html",{
                "val_err":forms.ValidationError('Username Already Exists!'),
                "form":newloginform()
                })
            elif password != re_pass:
                return render(request,"user/newlogin.html",{
                "val_err":forms.ValidationError('Password do not match'),
                "form":newloginform()
            })
            else:
                form=users(uname=uname,password=password)
                form.save()
                return HttpResponse("Success!!")

    return render (request,"user/newlogin.html",{
        "form":newloginform(),
        "newlogin":True
    })
