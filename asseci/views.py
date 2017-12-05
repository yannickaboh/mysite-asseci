from django.shortcuts import render

# Create your views here.


def accueil(request):
    return render(request, 'asseci/accueil.html', {})

def presentation(request):
    return render(request, 'asseci/presentation.html', {})
