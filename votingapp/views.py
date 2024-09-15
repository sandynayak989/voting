from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "home.html")

def register(request):
    if request.method == "POST":
        usn = request.POST['usn']
        email = request.POST['email']
        password = request.POST['psw']
    return render(request, "register.html")

def login(request):
    return render(request, "login.html")

def logout(request):
    pass