from django.conf.urls.defaults import *
from cms.models import Story, Category

info_dict = { 'queryset': Story.objects.all(), 'template_object_name': 'story' }


urlpatterns = patterns('cms.views',
    url(r'^category/(?P<slug>[-\w]+)/$', 'category', name="cms-category"),
    url(r'^search/$', 'search', name="cms-search"),
)

urlpatterns += patterns('django.views.generic.list_detail',
    url(r'^(?P<slug>[-\w]+)/$', 'object_detail', info_dict, name="cms-story"),
    url(r'^$', 'object_list', info_dict, name="cms-home"),
)
