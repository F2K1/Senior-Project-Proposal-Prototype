from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.template.response import TemplateResponse


def logIn(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        remember_checkbox = request.POST["remember_checkbox"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            args = {}
            args["username"] = username
            if remember_checkbox == True:
                request.session.set_expiry(300)
            return TemplateResponse(request, "main.html", args)
        else:
            messages.success(request, ("There was an error!"))
            return redirect("signin")

    else:
        return render(request, "login.html", {})
