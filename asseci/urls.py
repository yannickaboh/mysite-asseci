from django.conf.urls import url, include
from django.contrib import admin
from asseci import views
from . import views
from .views import EvenementListView, EvenementDetailView, AnnonceListView, AnnonceDetailView

app_name = 'asseci'



urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^$', views.accueil, name='accueil'),
    url(r'^presentation/$', views.presentation, name='presentation'),
    url(r'^presentation/le-bureau/$', views.bureau, name='bureau'),
    url(r'^presentation/nos-missions/$', views.missions, name='missions'),
    url(r'^promotion/id/$', views.membre, name='membre'),
    url(r'^promotion/membre/id/profil/$', views.membreId, name='membreId'),
    url(r'^actualites/evenement_list/$', EvenementListView.as_view(), name='evenement-list'),
    url(r'^actualites/evenement/(?P<pk>\d+)/$', EvenementDetailView.as_view(), name='evenement-detail'),
    url(r'^actualites/annonce_list/$', AnnonceListView.as_view(), name='annonce-list'),
    url(r'^actualites/annonce/(?P<pk>\d+)/$', AnnonceDetailView.as_view(), name='annonce-detail'),
    url(r'^actualites/timeline/$', views.timeline, name='timeline'),
    url(r'^mentions-legales/$', views.mentionslegales, name='mentionslegales'),
    url(r'^donation/$', views.paiement, name='paiement'),
    url(r'^plan-du-site/$', views.plan, name='plan'),

]