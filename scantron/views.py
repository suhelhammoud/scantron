from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 
    'scantron/index.html', 
    context={"name": "Suhel"})
    