from django.conf.urls.defaults import *
from demoapp import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^django_celery_demoproject/', include('django_celery_demoproject.foo.urls')),

    # (r'^admin/', include(admin.site.urls)),

    # (r'^demoproject/', include('demoproject.foo.urls')),
    (r'^admin/', include(admin.site.urls)),

    (r'^foo/', views.foo),

)
