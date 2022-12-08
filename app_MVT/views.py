from django.shortcuts import render

def familia(request):
    return render(request, 'app_mvt/index.html')