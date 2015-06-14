from django.conf.urls import url
from rpg_rest_api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^campaigns/$', views.CampaignList.as_view()),
    url(r'^campaigns/(?P<pk>[0-9]+)/$', views.CampaignDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

