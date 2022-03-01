from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse('AS- salaamu alaykum')

def new(request):
    return HttpResponse('salaam')
