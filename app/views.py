from django.shortcuts import render, redirect
from django.http import HttpResponse , JsonResponse 
from django.forms.models import model_to_dict 
from .data import *
unionData = Union_Data()

# Create your views here.

def home(request):
  return render(request, "app/home.html")
