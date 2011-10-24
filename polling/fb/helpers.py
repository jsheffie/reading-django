"""
Will Larson [ lethain@gmail.com ]
2007/12/4

Released under the GNU license.


A simple set of helper functions used for accessing Facebook
via the PyFacebook library, without using the PyFacebook
middleware.
"""

from django.conf import settings
import facebook.djangofb as facebook


def add_fb_instance(request):
    '''
    Intended to create an instances of facebook.Facebook to
    use to interact with the API for this specific session.
    '''
    # if already has a facebook instance, immediately return
    if getattr(request, 'facebook', None) is not None:
        return request

    # auth_token is other important possible param
    api_key = settings.FACEBOOK_API_KEY
    secret_key = settings.FACEBOOK_SECRET_KEY
    app_name = getattr(settings, 'FACEBOOK_APP_NAME', None)
    callback_path = getattr(settings, 'FACEBOOK_CALLBACK_PATH', None)
    internal = getattr(settings, 'FACEBOOK_INTERNAL', True)
    request.facebook = facebook.Facebook(
        api_key=api_key,
        secret_key=secret_key,
        app_name=app_name,
        callback_path=callback_path,
        internal=internal
        )


def require_fb_login(request, next=None):
    """
    Used for redirecting the user to the Facebook
    login page if not already logged in.

    Usage:
      redirect = require_fb_login(request)
      if redirect is not None: return redirect
    """
    if getattr(request, 'facebook', None) is None:
        add_fb_instance(request)
    fb = request.facebook
    if not fb.check_session(request):
        return fb.redirect(fb.get_login_url(next=next))


def require_fb_add(request, next=None):
    """
    Used for redirecting the user to the Facebook
    add-app page.

    Usage:
      redirect = require_fb_add(request)
      if redirect is not None: return redirect
    """
    if getattr(request, 'facebook', None) is None:
        add_fb_instance(request)
    fb = request.facebook
    if not fb.check_session(request):
        return fb.redirect(fb.get_login_url(next=next))
    if not fb.added:
        return fb.redirect(fb.get_add_url(next=next)) 


def get_fb_user(facebook):
    """
    Return the fb.models.User model instance associated with
    the @facebook parameter.

    Usage:
      user = get_fb_user(some_facebook_instance)
    """
    pass
    ### This portion must be updated for our specific models. ###
    """
    user, created = User.objects.get_or_create(facebook_id=int(facebook.uid))
     if the object is newly created
    if created is True:
        # get first and last name using FQL
        query = "SELECT uid, first_name, last_name FROM user WHERE uid=%s" % facebook.uid
        # FQL results a list of dicts, retrieve the first (and only) one
        results = facebook.fql.query(query)[0]
        user.name = "%s %s" % (results[u'first_name'], results[u'last_name'])
        user.save()
    return user
    """
