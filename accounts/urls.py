from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from views import *

urlpatterns = [
    url(r'^login/', auth_views.login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^logout/', auth_views.logout, {'template_name': 'accounts/logout.html'}, name='logout'),
    url(r'^register/', RegisterView.as_view(), name='register'),
    url(r'^password_change/', auth_views.password_change, name='password_change'),
    url(r'^password_change/done', auth_views.password_change_done, name='password_change_done'),
]