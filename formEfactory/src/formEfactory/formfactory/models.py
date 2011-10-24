from django.db import models


class FUser(models.Model):
    """ Used in the Create user form example."""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    
   
   
