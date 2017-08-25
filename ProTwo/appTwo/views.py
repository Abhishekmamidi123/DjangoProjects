# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
# from django.http import HttpResponse
from appTwo.models import User
from appTwo.forms import NewUserForm
# Create your views here.

def index(request):
    # return HttpResponse("<em>My Second Project<em>")
    return render(request, "appTwo/index.html")

def help(request):
    context = {"help_insert":"Welcome to Help Page"}
    return render(request, "appTwo/help.html", context=context)

def users(request):
    # all_users = User.objects.order_by('FirstName')
    # context = {"users":all_users}
    # return render(request, "appTwo/users.html", context=context)
    form = NewUserForm

    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)

    return render(request, "appTwo/users.html", {'form':form})
