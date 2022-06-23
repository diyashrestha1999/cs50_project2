from django.urls import reverse
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
class LoginForm(forms.Form):
    user_name=forms.CharField(label="Enter your user name:")
    user_email=forms.EmailField(label="Email:")
    password = forms.CharField(widget=forms.PasswordInput)    
def index(request):
    if "user_name" not in request.session:
        request.session["user_name"]=[]
    elif"user_email" not in request.session:
        request.session["user_email"]=[]
    elif "password" not in request.session:
        request.session["password"]=[]
    return render(request,"login/index.html",
    {"display_username":request.session["user_name"]},
    {"display_useremail":request.session["user_email"]},
    {"display_password":request.session["password"]})

def add(request):
    if request.method=="POST":
        new_form=LoginForm(request.POST)
        if new_form.is_valid:
            added_username=new_form.cleaned_data["user_name"]
            added_email=new_form.cleaned_data["user_email"]
            added_password=new_form.cleaned_data["password"]

            request.session["user_name"]+=[added_username]
            request.session["user_email"]+=[added_email]
            request.session["password"]+=[added_password]

            return HttpResponseRedirect(reverse("signup:index"))

    return render(request,"login/add.html",{"add_form":LoginForm()})