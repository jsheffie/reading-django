import datetime
from django.db import models
from django.db.models import permalink

class Paste(models.Model):
    """A single pastebin item"""
    
    SYNTAX_CHOICES = (
        (0, "Plain"), 
        (1, "XHTML"), 
        (2, "XML"), 
        (3, "JavaScript"),
        (4, "CSS"),
        (5, "Django"),
        (6, "Rails"),
        (7, "PHP"),
        (8, "SQL"), 
        (9, "HTML"), 
        (10, "XSLT"), 
        (11, "C"),
        (12, "Cpp"),
        (13, "C#"),
        (14, "Groovy"),
        (15, "Java"),
        (16, "JavaFx"),
        (17, "Pascal"),
        (18, "Perl"),
        (19, "Python"), 
        (20, "Ruby"),
        (21, "Erlang"),
        (22, "Scala"),
        (23, "VB"),
        (24, "Bash"),
        (25, "Patch"),
        (26, "PowerShell"),
        (27, "AppleScript"),
        (28, "ActionScript3"),
        (29, "Sass"),
        (30, "ColdFusion"),        
        )

    content   = models.TextField()
    title     = models.CharField(blank=True, max_length=30)
    syntax    = models.IntegerField(max_length=30, choices=SYNTAX_CHOICES, default=0)
    poster    = models.CharField(blank=True, max_length=30)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
        
    class Meta:
        ordering = ('-timestamp',)
        
    def __unicode__(self):
        return "%s (%s)" % (self.title or "#%s" % self.id, self.get_syntax_display()) 

    @permalink
    def get_absolute_url(self):
        return ('django.views.generic.list_detail.object_detail', 
            None, {'object_id': self.id})

