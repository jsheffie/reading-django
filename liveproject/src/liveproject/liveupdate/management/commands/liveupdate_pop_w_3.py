## http://docs.djangoproject.com/en/dev/howto/custom-management-commands/
from django.core.management.base import NoArgsCommand, CommandError
from liveupdate.models import Update
import time

class Command(NoArgsCommand):
    requires_model_validation = False
    ts = time.time()
    def handle_noargs(self, **options):
        new_update = Update(text="an update")
        new_update.save()
        
        foo_update = Update(text="foo an update")
        foo_update.save()
        bar_update = Update(text="bar an update")
        bar_update.save()
        
