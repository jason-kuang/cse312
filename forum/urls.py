from django.urls import path

from . import views

urlpatterns = [
    path('', views.render_forum, name='forum'),
    path('online', views.renderOnline, name='online')
]