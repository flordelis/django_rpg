from django.conf.urls import url
from rpg_api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^campaigns/$', views.CampaignList.as_view()),
    url(r'^campaigns/(?P<pk>[0-9]+)/$', views.CampaignDetail.as_view()),
    url(r'^characters/$', views.CharacterList.as_view()),
    url(r'^characters/(?P<pk>[0-9]+)/$', views.CharacterDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

