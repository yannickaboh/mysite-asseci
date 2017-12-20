from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login

from .forms import SignUpForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('asseci:accueil')
    else:
        form = SignUpForm()
    return render(request, 'asseci/signup.html', {'form': form})


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Votre mot de passe a été correctement mis à jour!!!')
            return redirect('asseci:change_password')
        else:
            messages.error(request, 'SVP, saisissez correctemment vos mots de passe')
    else:
        form = PasswordChangeForm(request.POST)
    return render(request, 'asseci/change_password.html', {'form': form})



#@method_decorator(login_required, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ('username','first_name', 'last_name', 'email', )
    template_name = 'asseci/mon_compte.html'
    success_url = reverse_lazy('asseci:my_account')

    def get_object(self):
        return self.request.user