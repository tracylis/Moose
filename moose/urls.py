from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from moose import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'moose.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'', 'moose.views.test1'),
    url(r'^(\d{4})/$', 'moose.views.test1'),
    url(r'^admin/', include(admin.site.urls)),
)