from django.conf.urls import include, url
from django.contrib import admin
import rpg_base.urls

urlpatterns = [
    # Examples:
    # url(r'^$', 'django_rpg.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(rpg_base.urls)),
]
