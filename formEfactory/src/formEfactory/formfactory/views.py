from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.shortcuts import render_to_response
from formfactory.models import FUser

def index(request):
    return render_to_response('formfactory/index.html', )
 
def create_user(request):
    """ receiving an ajax request with json data, representing 
    username, email, password. ( no validation required, that was done
    on the client side."""
    users = FUser.objects.all()
    return render_to_response('formfactory/create_user.html', {'users': users })

def old_xhr_test(request):
    if request.is_ajax():
        message = "Hello AJAX"
    else:
        message = "Hello"
    return HttpResponse(message)


def xhr_test(request):
    if request.is_ajax():
        if request.method == 'GET':
            message = "This is an XHR GET request"
        elif request.method == 'POST':
            message = "This is an XHR POST request"
            # Here we can access the POST data
            print request.POST
            print request.POST['name']
            nuser = FUser(name = request.POST['name'],
                          password = request.POST['password'],
                          email = request.POST['email'],
                          )
            nuser.save()
            return HttpResponseRedirect("/")
    else:
        message = "No XHR"

    return HttpResponse(message)
