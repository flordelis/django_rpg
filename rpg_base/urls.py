from django.conf.urls import include, url
from rpg_base.views import *

urlpatterns = [
    # Examples:
    # url(r'^$', 'django_rpg.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', campaign.index, name='campaign_index'),
    url(r'^(?P<pk>[0-9]+)/$', campaign.view, name='campaign_view'),
    url(r'^(?P<pk>[0-9]+)/character/$', character.index, name='character_index'),
    url(r'^(?P<pk>[0-9]+)/character/(?P<character_pk>[0-9]+)$', character.view, name='character_view'),

    # TODO This is going to get messy super quick.
]