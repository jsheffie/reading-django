from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_list, object_detail
from django.views.generic.create_update import create_object
from pastebin.models import Paste
from django.conf import settings
import os

display_info = {'queryset': Paste.objects.all()}
create_info  = {'model': Paste}

urlpatterns = patterns('',
                      (r'^css/(.*)$', 'django.views.static.serve', {'document_root': os.path.join(settings.MEDIA_ROOT, "css")}),
                      (r'^styles/(.*)$', 'django.views.static.serve', {'document_root': os.path.join(settings.MEDIA_ROOT, "css")}),
                      (r'^js/(.*)$',  'django.views.static.serve', {'document_root': os.path.join(settings.MEDIA_ROOT, "js")}),
                      (r'^img/(.*)$', 'django.views.static.serve', {'document_root': os.path.join(settings.MEDIA_ROOT, "img")}),
                      (r'^jst/(.*)$', 'django.views.static.serve', {'document_root': os.path.join(settings.MEDIA_ROOT, "jst")}),
                      url(r'^$', object_list, dict(display_info, allow_empty=True)),
                      url(r'^(?P<object_id>\d+)/$', object_detail, display_info),
                      url(r'^add/$', create_object, create_info),
)
