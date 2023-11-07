from django.shortcuts import render
from django.http import HttpResponse


def homeSI(req):
    return render(req, "core/index.html")