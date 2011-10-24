from django.contrib import admin
#from rel_web.repo.models import *
from formEfactory.formfactory.models import FUser


admin.site.register(FUser)

# JDS: guide used to add the createrepo stuff
# 1:   http://www.beardygeek.com/2010/03/adding-views-to-the-django-admin/
# 2.1: http://www.charlesleifer.com/blog/using-class-based-views-effectively/
# 2.2: http://forum.webfaction.com/viewtopic.php?pid=15489
