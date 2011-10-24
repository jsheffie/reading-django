import unittest
from django.test.client import Client
from polling.core.models import Poll, User
from polling.core.forms import PollForm


MODELS = [Poll, User]


class CoreModelTest(unittest.TestCase):
    "Test the models contained in the 'core' app."

    def setUp(self):
        'Populate test database with model instances.'
        self.client = Client()
        wl = User(name="Will Larson")
        wl.save()
        jb = User(name="Jack Bauer")
        jb.save()
        bc = User(name="Bill Clinton")
        bc.save()
        Poll(question="Did you vote for me?", creator=bc).save()
        Poll(question="Am I human?", creator=jb).save()
        Poll(question="Are you still reading?", creator=wl).save()

    def tearDown(self):
        'Depopulate created model instances from test database.'
        for model in MODELS:
            for obj in model.objects.all():
                obj.delete()

    def test_poll(self):
        "This is a test for the polling.core.models.Poll model."
        poll = Poll.objects.get(pk=1)
        up = poll.up_votes
        down = poll.down_votes
        self.assertEquals(up, poll.up_votes)
        self.assertEquals(down, poll.up_votes)
        self.assertEquals(up-down, poll.score())
        poll.up()
        up = up + 1
        self.assertEquals(up, poll.up_votes)
        poll.down()
        down = down + 1
        self.assertEquals(down, poll.down_votes)
        self.assertEquals(up-down, poll.score())

    def test_user(self):
        "This is a test for the polling.core.models.User model."
        user = User.objects.get(pk=1)
        p = user.create_poll("Is this actually working?")
        self.assertEquals(user, p.creator)


class CoreFormTest(unittest.TestCase):
    "Test the forms contained in the 'core' app."

    def test_PollForm(self):
        f = PollForm()
        self.assertEquals(False, f.is_valid())
        data = {}
        f = PollForm(data)
        self.assertEquals(False, f.is_valid())
        self.assertEquals([u'This field is required.'], f.errors['question'])
        data = {"question":"Is this valid?"}
        f = PollForm(data)
        self.assertEquals(True, f.is_valid())
        self.assertEquals("Is this valid?", f.cleaned_data['question'])
        u = User(name="Will L")
        u.save()
        p = Poll(question="Is it real?", creator=u)
        p.save()
        data = {"question":"Is it real?"}
        f = PollForm(data)
        # should be false because Poll with this question already
        # exists in our database
        self.assertEquals(False, f.is_valid())
        self.assertEquals([u'The question "Is it real?" is already in use.'], f.errors['question'])
        p.delete()
        u.delete()
