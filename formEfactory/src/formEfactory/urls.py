from django.conf.urls.defaults import patterns, include, url
from formEfactory import formfactory


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'formEfactory.views.home', name='home'),
    # url(r'^formEfactory/', include('formEfactory.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', include('formfactory.urls')),
    (r'^$',            'formfactory.views.index'),
    (r'^create_user/$', 'formfactory.views.create_user'), 
    (r'^xhr_test/$',   'formfactory.views.xhr_test'),
)
from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('',
                            (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                             {'document_root': settings.MEDIA_ROOT}),
                            )
    