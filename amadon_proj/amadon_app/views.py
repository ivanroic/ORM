from django.shortcuts import render

def index(request):
    return render(request, 'amadon_app/index.html')
