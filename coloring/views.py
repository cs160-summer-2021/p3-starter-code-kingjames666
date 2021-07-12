from django.shortcuts import render

def frame1(request):
    return render(request, 'coloring/frame1.html')

def frame2(request):
    return render(request, 'coloring/frame2.html')

def index(request):
    return render(request, 'coloring/index.html')
