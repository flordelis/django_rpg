from django.conf.urls import include, url
from django.contrib import admin
import rpg_base.urls
import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'django_rpg.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name="index"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^campaign/', include(rpg_base.urls)),

]
