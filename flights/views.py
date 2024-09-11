from django.shortcuts import render
from django.http import HttpResponse
from .models import Flight
# Create your views here.

def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })


