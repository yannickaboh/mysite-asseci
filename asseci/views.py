from django.shortcuts import get_object_or_404, render, redirect, render_to_response
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse

from django.views import generic
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.db.models import Count

from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.utils import timezone

#from django.contrib.auth.decorators import login_required
#from django.utils.decorators import method_decorator

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.forms import ModelForm
#from .forms import EvenementForm
import re
from django.db.models import Q
from django.template.loader import render_to_string

from .models import Evenement, Annonce, ThemeForum, Board, Topic, Post

from django.contrib.auth.models import User

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

# Evenements
class EvenementListView(ListView):

    model = Evenement

    def get_context_data(self, **kwargs):
        context = super(EvenementListView, self).get_context_data(**kwargs)
        return context

# Evenement DetailView
class EvenementDetailView(DetailView):

    model = Evenement

    def get_context_data(self, **kwargs):
        context = super(EvenementDetailView, self).get_context_data(**kwargs)
        success_url = reverse_lazy('asseci:evenement_list')
        return context

# Annonce List View
class AnnonceListView(ListView):

    model = Annonce

    def get_context_data(self, **kwargs):
        context = super(AnnonceListView, self).get_context_data(**kwargs)
        return context

# Annonce DetailView
class AnnonceDetailView(DetailView):

    model = Annonce

    def get_context_data(self, **kwargs):
        context = super(AnnonceDetailView, self).get_context_data(**kwargs)
        success_url = reverse_lazy('asseci:annonce_list')
        return context

# Actualités / Timeline
def timeline(request):
	evenement = Evenement.objects.all()
	annonces = Annonce.objects.all()
	return render(request, 'asseci/timeline.html', {'evenement' : evenement, 'annonces' : annonces,  })