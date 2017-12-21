from django.conf.urls import url, include
from django.contrib import admin
from asseci import views
from . import views
from .views import EvenementListView, EvenementDetailView, AnnonceListView, AnnonceDetailView, ForumListView


from accounts import views as accounts_views

from django.contrib.auth import views as auth_views

app_name = 'asseci'



urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^$', views.accueil, name='accueil'),
    url(r'^presentation/$', views.presentation, name='presentation'),
    url(r'^presentation/le-bureau/$', views.bureau, name='bureau'),
    url(r'^presentation/nos-missions/$', views.missions, name='missions'),
    url(r'^promotion/id/$', views.membre, name='membre'),
    url(r'^promotion/id/2/$', views.membre2, name='membre2'),
    url(r'^promotion/membre/id/profil/$', views.membreId, name='membreId'),
    url(r'^actualites/evenement_list/$', EvenementListView.as_view(), name='evenement-list'),
    url(r'^actualites/evenement/(?P<pk>\d+)/$', EvenementDetailView.as_view(), name='evenement-detail'),
    url(r'^actualites/annonce_list/$', AnnonceListView.as_view(), name='annonce-list'),
    url(r'^actualites/annonce/(?P<pk>\d+)/$', AnnonceDetailView.as_view(), name='annonce-detail'),
    url(r'^actualites/timeline/$', views.timeline, name='timeline'),
    url(r'^mentions-legales/$', views.mentionslegales, name='mentionslegales'),
    url(r'^donation/$', views.paiement, name='paiement'),
    url(r'^plan-du-site/$', views.plan, name='plan'),
    url(r'^contact/$', views.contact, name='contact'),
    
    url(r'^tableau-de-bord/$', views.dashboard, name='dashboard'),
    url(r'^tableau-de-bord/infos-personnelles/$', accounts_views.UserUpdateView.as_view(), name='my_account'),
    url(r'^tableau-de-bord/changer-mot-de-passe/$', accounts_views.change_password, name='change_password'),

    url(r'^contacts/formulaire/$', views.ContactezNous, name='contacteznous'),

    url(r'^tableau-de-bord/infos-persos/(?P<pk>\d+)/$', views.infos_persos, name='infos-persos'),

    # FORUM
    #url(r'^forum/$', views.forum, name='forum'),
    url(r'^forum/themes/$', views.ForumListView.as_view(), name='forum'),
    url(r'^inscription/$', accounts_views.signup, name='signup'),
    
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='asseci/login.html'), name='login'),
    #url(r'^themes/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
    url(r'^themes/(?P<pk>\d+)/nouveau/$', views.new_topic, name='new_topic'),
    url(r'^themes/(?P<pk>\d+)/sujets/(?P<topic_pk>\d+)/$', views.topic_posts, name='topic_posts'),
    url(r'^themes/(?P<pk>\d+)/sujets/(?P<topic_pk>\d+)/repondre/$', views.reply_topic, name='reply_topic'),
    url(r'^nouveau_post/$', views.NewPostView.as_view(), name='new_post'),
    url(r'^themes/(?P<pk>\d+)/sujets/(?P<topic_pk>\d+)/commentaires/(?P<post_pk>\d+)/editer/$',
        views.PostUpdateView.as_view(), name='edit_post'),
    url(r'^themes/(?P<pk>\d+)/$', views.TopicListView.as_view(), name='board_topics'),
    url(r'^themes/(?P<pk>\d+)/sujets/(?P<topic_pk>\d+)/$', views.PostListView.as_view(), name='topic_posts'),


    url(r'^settings/password/$', auth_views.PasswordChangeView.as_view(template_name='asseci/password_change.html'),
    name='password_change'),
    url(r'^settings/password/done/$', auth_views.PasswordChangeDoneView.as_view(template_name='asseci/password_change_done.html'),
        name='password_change_done'),

    url(r'^reset/$',
    auth_views.PasswordResetView.as_view(
        template_name='asseci/password_reset.html',
        email_template_name='asseci/password_reset_email.html',
        subject_template_name='asseci/password_reset_subject.txt'
    ),
    name='password_reset'),
    url(r'^reset/done/$',
        auth_views.PasswordResetDoneView.as_view(template_name='asseci/password_reset_done.html'),
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(template_name='asseci/password_reset_confirm.html'),
        name='password_reset_confirm'),
    url(r'^reset/complete/$',
        auth_views.PasswordResetCompleteView.as_view(template_name='asseci/password_reset_complete.html'),
        name='password_reset_complete'),

]