from models import Tweet
from django.shortcuts import render_to_response
from django.template import RequestContext

def public(request):
    return render_to_response('twitter/public.html', 
                              {'tweets': Tweet.objects.order_by('-date_posted')},
                              context_instance = RequestContext(request))