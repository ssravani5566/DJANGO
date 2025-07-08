
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def aliya(request):
    return render(request, 'aliya.html')

def sravani(request):
    return render(request, 'sravani.html')

def pavani(request):
    return render(request, 'pavani.html')

def varsha(request):
    return render(request, 'varsha.html')

def pinky(request):
    return render(request, 'pinky.html')



# Create your views here.
