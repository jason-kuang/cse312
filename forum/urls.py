from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('online', views.renderOnline, name='online'),
    path('signup/', views.signup, name='signup'),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('profile', views.update_profile, name='profile')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)