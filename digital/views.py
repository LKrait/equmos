from django.shortcuts import render


def home(request):
    return render(request, 'digital/index.html')


def labs(request):
    return render(request, 'labs.html')

