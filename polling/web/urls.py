from django.conf.urls.defaults import *
from polling.core.models import *

polls = Poll.objects.all()

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.list_detail.object_list', 
     dict(template_name='web/poll_list.html', queryset=polls)),
    (r'^poll/(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail',
     dict(template_name='web/poll_detail.html', queryset=polls)),
    (r'^create/$', 'polling.web.views.create'),
    (r'^vote/$', 'polling.web.views.vote')
)
