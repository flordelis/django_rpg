from django.conf.urls import include, url
from rpg_base.views import *

urlpatterns = [
    # Examples:
    # url(r'^$', 'django_rpg.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'campaigns/$', campaign.index, name='index'),
    url(r'campaigns/(?P<pk>[0-9]+)/$', campaign.view, name='campaign_view'),
]