from django.contrib import admin
#from rel_web.repo.models import *
from photo_gallery.gallery.models import Photo, Item

class PhotoInLine(admin.StackedInline):
    model = Photo

class ItemAdmin(admin.ModelAdmin):
    inlines = [PhotoInLine]

admin.site.register(Item, ItemAdmin)
admin.site.register(Photo)
