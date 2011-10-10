from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'^pastebin/', include('samplesite.pastebin.urls')),
    (r'^paste/', include('samplesite.pastebin.urls')),
    (r'^admin/', include(admin.site.urls)),
)
