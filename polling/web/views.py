from django.utils import simplejson
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.simple import direct_to_template
from polling.core.models import Poll, User
from polling.core.forms import PollForm


def create(request):
    if request.method == 'POST':
        form = PollForm(request.POST)
        if form.is_valid():
            u = User(name="Some name")
            u.save()
            poll = Poll(creator=u, question=form.cleaned_data['question'])
            poll.save()
            return HttpResponseRedirect('/')
    else:
        form = PollForm()
    return direct_to_template(request, 'web/create.html',
                              extra_context={'form':form})


def vote(request):
    result = {'success':False}
    if request.method == u'GET':
        GET = request.GET
        if GET.has_key(u'pk') and GET.has_key(u'vote'):
            pk = int(GET[u'pk'])
            vote = GET[u'vote']
            poll = Poll.objects.get(pk=pk)
            if vote == u"up":
                poll.up()
            elif vote == u"down":
                poll.down()
            results = {'success':True}
    json = simplejson.dumps(results)
    return HttpResponse(json, mimetype='application/json')

    
            
