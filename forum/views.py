# Views are Python functions that receive an HttpRequest object
# and returns an HttpResponse object. Receive a request as a parameter
# and returns a response as a result.
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.shortcuts import render, redirect
from django.http import HttpResponse

from online_users.models import OnlineUserActivity

from .forms import UserForm, ProfileForm
from .models import Board, Topic


def index(request):
    boards = Board.objects.all()
    return render(request, 'index.html', {'boards': boards})


def renderOnline(request):
    onlines = OnlineUserActivity.get_user_activities()
    number = onlines.count()
    return render(request, 'online.html', {'online': onlines, 'count': number})


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            #messages.success(request, _('Your profile was successfully updated!'))
            return redirect('profile')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.userprofile)
    return render(request, 'profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

def logout(request):
    return render(request,'logged_out.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})