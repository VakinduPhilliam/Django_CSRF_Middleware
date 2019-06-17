# Python Cross Site Request Forgery protection (CSRF Protection) with Django
# The CSRF middleware and template tag provides easy-to-use protection against Cross Site Request Forgeries. 
# This type of attack occurs when a malicious website contains a link, a form button or some JavaScript that is intended to
# perform some action on your website, using the credentials of a logged-in user who visits the malicious site in their
# browser. 
# The first defense against CSRF attacks is to ensure that GET requests (and other ‘safe’ methods, as defined by RFC) are side effect free.
#

#
# Testing:
# The CsrfViewMiddleware will usually be a big hindrance to testing view functions, due to the need for the CSRF
# token which must be sent with every POST request.
# For this reason, Django’s HTTP client for tests has been modified to set a flag on requests which relaxes the middleware and the csrf_protect decorator
# so that they no longer rejects requests.
# In every other respect (e.g. sending cookies etc.), they behave the same.
#

#
# If, for some reason, you want the test client to perform CSRF checks, you can create an instance of the test client that enforces CSRF checks:
#

from django.test import Client

csrf_client = Client(enforce_csrf_checks=True)