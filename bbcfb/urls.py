from django.conf.urls import patterns, include, url
import showphoto
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bbcfb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^showphoto/', include('showphoto.urls')),
    url(r'^admin/', include(admin.site.urls)),

)
