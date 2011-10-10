from django.contrib import admin
from samplesite.cms.models import Category, Story

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('label',)}

class StoryAdmin(admin.ModelAdmin):
    list_display        = ('title', 'owner', 'status', 'created', 'modified')
    search_fields       = ('title', 'content')
    list_filter         = ('status', 'owner', 'created', 'modified')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Story, StoryAdmin)

admin.site.register(Category, CategoryAdmin)
