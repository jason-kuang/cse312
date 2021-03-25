# Views are Python functions that receive an HttpRequest object
# and returns an HttpResponse object. Receive a request as a parameter
# and returns a response as a result.

from django.shortcuts import render
from django.http import HttpResponse

from online_users.models import OnlineUserActivity
from .models import Board, Topic


def render_forum(request):
    boards = Board.objects.all()
    return render(request, 'forum.html', {'boards': boards})


def renderOnline(request):
    onlines = OnlineUserActivity.get_user_activities()
    number = onlines.count()
    return render(request, 'online.html', {'online': onlines, 'count': number})
