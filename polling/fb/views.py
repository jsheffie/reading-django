from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.simple import direct_to_template
from django.shortcuts import get_object_or_404
from django.utils import simplejson
from polling.fb.helpers import *
from polling.core.models import *
