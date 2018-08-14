from django.shortcuts import render

from .models import Beregning1

def home(request):
    Step1 = Beregning1.objects
    return render(request, 'Step1/home.html')
