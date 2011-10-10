from django.shortcuts import render_to_response
from photo_gallery.gallery.models import Photo, Item

# Create your views here.
def index(request):
    item_list = Item.objects.all()
    return render_to_response('gallery/index.html', {
        'item_list': item_list,
    })
    
    