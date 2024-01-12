from django.shortcuts import render
from django.views import View


def init_base(request):
    return render(request, "accounts/base.html")


def init_index(request):
    return render(request, "accounts/index.html")