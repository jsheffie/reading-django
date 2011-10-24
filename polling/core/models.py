from django.db import models
from django.contrib.auth.models import User as DjangoUser


class Poll(models.Model):
    """
    Model used for tracking polls and responses to the poll.
    """
    question = models.CharField(unique=True, max_length=200)
    creator = models.ForeignKey('User')
    up_votes = models.IntegerField()
    down_votes = models.IntegerField()

    class Admin:
        pass

    def score(self):
        return self.up_votes - self.down_votes

    def up(self):
        self.up_votes = self.up_votes + 1
        self.save()

    def down(self):
        self.down_votes = self.down_votes + 1
        self.save()

    def save(self):
        """Overriding save() to innitialize values for up_votes and down_votes."""
        if not self.up_votes:
            self.up_votes = 0
        if not self.down_votes:
            self.down_votes = 0
        return super(Poll, self).save()

    def __unicode__(self): 
        return "%s asked by %s" % (self.question, self.creator)


class User(models.Model):
    """
    Model used for associating Facebook User IDs or
    django.contrib.auth.models.User instances with
    actions performed on our system.

    Only one of 'user' and 'facebook_id' should have a
    non-null value. Facebook users will not have an
    associated User, and regular web users will not
    have a 'facebook_id'.
    """
    user = models.ForeignKey(DjangoUser, blank=True, null=True)
    facebook_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=200)

    class Admin:
        pass

    def create_poll(self, question):
        p = Poll(creator=self, question=question)
        p.save()
        return p

    def __unicode__(self):
        return self.name
