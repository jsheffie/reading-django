from django.db import models

# Create your models here.


class Author(models.Model):
    firstname = models.CharField()
    lastname  = models.CharField()
    website   = models.URLField(blank=True, verify_exists=True)
    email     = models.EmailField(blank=True)
    