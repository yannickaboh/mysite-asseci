from django.shortcuts import render

# Create your views here.


# Accueil
def accueil(request):
    return render(request, 'asseci/accueil.html', {})

# Presentation
def presentation(request):
    return render(request, 'asseci/presentation.html', {})

# Presentation / Mission
def missions(request):
	return render(request, 'asseci/missions.html', {})

# Presentation / Bureau
def bureau(request):
	return render(request, 'asseci/bureau.html', {})

# Profils & Membres
def membre(request):
	return render(request, 'asseci/membre.html', {})

# Profils & Membres / Id
def membreId(request):
	return render(request, 'asseci/membreId.html', {})
