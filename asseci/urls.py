from django.conf.urls import url, include
from django.contrib import admin
from asseci import views

app_name = 'asseci'



urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^$', views.accueil, name='accueil'),
    url(r'^presentation/$', views.presentation, name='presentation'),

]