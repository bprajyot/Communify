from django.http import HttpResponse
from django.shortcuts import render, redirect

def Index(request):
     return render(request,"index.html")

def Login(request):
     return render(request,"registration/login.html")

def Create(request):
     return render(request,"create.html")

def Message(request):
     return render(request,"message.html")

def Post(request):
     return render(request,"post.html")

def About(request):
     return render(request,"about.html")

def Forgotpass(request):
     return render(request,"forgot_pass.html")

def Contact(request):
     return render(request,"contact.html")

def feed_redirect(request):
    return redirect('/feed')