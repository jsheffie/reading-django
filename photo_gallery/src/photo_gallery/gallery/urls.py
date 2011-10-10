from django.conf.urls.defaults import patterns, url

from gallery.models import Item, Photo

#urlpatterns = patterns('',
#                       #(r'^$',  'photo_gallery.gallery.views.index'),
urlpatterns = patterns('django.views.generic',
                       url(r'^$', 'simple.direct_to_template', 
                           kwargs={
                                   'template': 'gallery/index.html',
                                   'extra_context': {'item_list': lambda: Item.objects.all()}
                                   },
                           name='index'
                           ),
                       
                        url(r'^items/$', 'list_detail.object_list',
                            kwargs={
                                    'queryset': Item.objects.all(),
                                    'template_name': 'gallery/items_list.html',
                                    'allow_empty': True
                                    },
                            name='item_list'
                            ),
                       url(r'^items/(?P<object_id>\d+)/$', 'list_detail.object_detail',
                           kwargs={
                                   'queryset': Item.objects.all(),
                                   'template_name': 'gallery/items_detail.html'
                                   },
                           name='item_detail'
                           ),
                       url(r'^photos/(?P<object_id>\d+)/$', 'list_detail.object_detail', 
                           kwargs={
                                   'queryset': Photo.objects.all(),
                                   'template_name': 'gallery/photos_detail.html'
                                   },
                           name='photo_detail'
                           ),
                       )

    