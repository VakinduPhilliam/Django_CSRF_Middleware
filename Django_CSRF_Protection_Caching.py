# Python Cross Site Request Forgery protection (CSRF Protection) with Django
# The CSRF middleware and template tag provides easy-to-use protection against Cross Site Request Forgeries. 
# This type of attack occurs when a malicious website contains a link, a form button or some JavaScript that is intended to
# perform some action on your website, using the credentials of a logged-in user who visits the malicious site in their
# browser. 
# The first defense against CSRF attacks is to ensure that GET requests (and other ‘safe’ methods, as defined by RFC) are side effect free.
#

#
# Caching:
# If the csrf_token template tag is used by a template (or the get_token function is called some other way), CsrfViewMiddleware will add a cookie and
# a Vary: Cookie header to the response. 
# This means that the middleware will play well with the cache middleware if it is used as instructed (UpdateCacheMiddleware goes before all other
# middleware).
#

#
# However, if you use cache decorators on individual views, the CSRF middleware will not yet have been able to set the Vary header or the CSRF cookie, and
# the response will be cached without either one.
# In this case, on any views that will require a CSRF token to be inserted you should use the django.views.decorators.csrf.csrf_protect() decorator first:
#

from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect

@cache_page(60 * 15)
@csrf_protect

def my_view(request):

# ...
