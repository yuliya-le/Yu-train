from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def about(request):
    context = {'title': 'О тренажере'}
    return render(request, 'main/about.html', context)

def dashboard(request):
    context = {'title': 'Доска почета'}
    return render(request, 'main/dashboard.html', context)

def new(request):
    context = {'title': 'Новая страница'}
    return render(request, 'main/new.html', context)