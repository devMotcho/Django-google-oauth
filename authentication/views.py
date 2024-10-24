from django.shortcuts import render, redirect
from django.contrib.auth import logout

def homePage(request):
    context = {}
    return render(request, 'home.html', context)


def logoutView(request):
    logout(request)
    return redirect("authentication:home")