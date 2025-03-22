from django.shortcuts import render


def home(request):
    return render(request, 'digital/index.html')


def labs(request):
    return render(request, 'digital/labs.html')


def acc(request):
    return render(request, 'digital/login.html')


