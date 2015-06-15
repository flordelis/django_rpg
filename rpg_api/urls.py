from django.conf.urls import url
from rpg_api import views
from rest_framework.urlpatterns import format_suffix_patterns

from django.conf.urls import url, include
from rpg_api import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'campaigns', views.CampaignViewSet)

router.register(r'characters', views.CharacterViewSet)
router.register(r'races', views.RaceViewSet)
router.register(r'hit_die', views.HitDieViewSet)
router.register(r'character_templates', views.CharacterTemplateViewSet)
router.register(r'classes', views.DndClassViewSet)

router.register(r'locations', views.LocationViewSet)
router.register(r'organizations', views.OrganizationViewSet)
router.register(r'user', views.UserViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]


