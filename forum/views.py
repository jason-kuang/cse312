# Views are Python functions that receive an HttpRequest object
# and returns an HttpResponse object. Receive a request as a parameter
# and returns a response as a result.

from django.shortcuts import render
from django.http import HttpResponse
from .models import Board


# Create your views here.
def render_forum(request):
    boards = Board.objects.all()
    return render(request, 'forum.html', {'boards': boards})
