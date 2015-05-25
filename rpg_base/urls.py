from django.conf.urls import include, url
from rpg_base.views import *

urlpatterns = [
    # Examples:
    # url(r'^$', 'django_rpg.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', campaign.index, name='campaign_index'),
    url(r'^create/$', campaign.create, name='campaign_create'),
    url(r'^(?P<campaign_pk>[0-9]+)/$', campaign.view, name='campaign_view'),

    url(r'^(?P<campaign_pk>[0-9]+)/character/$', character.index, name='character_index'),
    url(r'^(?P<campaign_pk>[0-9]+)/character/(?P<character_pk>[0-9]+)$', character.view, name='character_view'),

    url(r'^(?P<campaign_pk>[0-9]+)/location/$', location.index, name='location_index'),
    url(r'^(?P<campaign_pk>[0-9]+)/location/(?P<location_pk>[0-9]+)$', location.view, name='location_view'),
    # TODO This is going to get messy super quick.

    url(r'^(?P<campaign_pk>[0-9]+)/encounter/$', encounter.index, name='encounter_index'),
    url(r'^(?P<campaign_pk>[0-9]+)/encounter/(?P<encounter_pk>[0-9]+)$', encounter.view, name='encounter_view'),

    url(r'^(?P<campaign_pk>[0-9]+)/organization/$', organization.index, name='organization_index'),
    url(r'^(?P<campaign_pk>[0-9]+)/organization/(?P<organization_pk>[0-9]+)$', organization.view, name='organization_view'),
]