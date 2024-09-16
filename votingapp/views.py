from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.
def home(request):
    return render(request, "home.html")

def register(request):
    if request.method == "POST":
        usn = request.POST['usn']
        fname = request.POST['fname']
        email = request.POST['email']
        password = request.POST['password']

        myuser = User.objects.create_user(usn,email,password)
        myuser.full_name = fname

        myuser.save()

        messages.success(request, "Your account has been successfully created!")
        return redirect('signin')

    return render(request, "register.html")

def signin(request):
    if request.method == 'POST':
        usn = request.POST['usn']
        password = request.POST['password']

        user = authenticate(usn = usn, password = password)

        if user is not None:
            login(request, user)
            fname = user.full_name
            return redirect(request, 'home.html', {'fname': fname})
        else:
            messages.error(request, "Wrong Credentials!")
            return redirect('signin')

    return render(request, "login.html")

def logout(request):
    pass