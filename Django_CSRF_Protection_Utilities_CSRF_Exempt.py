# Python Cross Site Request Forgery protection (CSRF Protection) with Django
# The CSRF middleware and template tag provides easy-to-use protection against Cross Site Request Forgeries. 
# This type of attack occurs when a malicious website contains a link, a form button or some JavaScript that is intended to
# perform some action on your website, using the credentials of a logged-in user who visits the malicious site in their
# browser. 
# The first defense against CSRF attacks is to ensure that GET requests (and other ‘safe’ methods, as defined by RFC) are side effect free.
#

#
# Utilities.
# csrf_exempt(view)
# This decorator marks a view as being exempt from the protection ensured by the middleware.
#

#
# Example:
#

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def my_view(request):

return HttpResponse('Hello world')
