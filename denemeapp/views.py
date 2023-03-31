from django.shortcuts import render

def index(request):
    return render(request, 'denemeapp/index.html')


def generic(request):
    return render(request, 'denemeapp/generic.html')

def elements(request):
    return render(request, 'denemeapp/elements.html')