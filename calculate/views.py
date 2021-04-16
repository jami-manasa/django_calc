from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'calculate/home.html')


def js(request):
    return render(request, 'calculate/home.html')
