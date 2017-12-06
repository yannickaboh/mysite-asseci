from django.conf.urls import url, include
from django.contrib import admin
from asseci import views

app_name = 'asseci'



urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^$', views.accueil, name='accueil'),
    url(r'^presentation/$', views.presentation, name='presentation'),
    url(r'^presentation/le-bureau/$', views.bureau, name='bureau'),
    url(r'^presentation/nos-missions/$', views.missions, name='missions'),
    url(r'^promotion/id/$', views.membre, name='membre'),
    url(r'^promotion/membre/id/profil/$', views.membreId, name='membreId'),

]