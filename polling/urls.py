from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/Users/will/django/polling/media/'}),
    (r'^admin/', include('django.contrib.admin.urls')),
    (r'^facebook/', include('polling.fb.urls')),
    (r'^', include('polling.web.urls')),
)
