from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User


def loadPage(request):
    return render(request, "signin.html", {})
    
def signIn(request):
    if request.method == "POST":
        username = request.POST["username"]
        name = request.POST["name"]
        surname = request.POST["surname"]
        email = request.POST["email"]
        password = request.POST['password']
        user = User.objects.create_user(username, first_name=name, last_name=surname, email=email, password=password)
        if user is not None:
            return redirect("/")
        else:
            messages.success(request, ("There was an error!"))
            return redirect("signin")

    else:
        return render(request, "signin.html", {})
