# Python Cross Site Request Forgery protection (CSRF Protection) with Django
# The CSRF middleware and template tag provides easy-to-use protection against Cross Site Request Forgeries. 
# This type of attack occurs when a malicious website contains a link, a form button or some JavaScript that is intended to
# perform some action on your website, using the credentials of a logged-in user who visits the malicious site in their
# browser. 
# The first defense against CSRF attacks is to ensure that GET requests (and other ‘safe’ methods, as defined by RFC) are side effect free.
#

#
# Utilities.
# requires_csrf_token(view)
# Normally the csrf_token template tag will not work if CsrfViewMiddleware.process_view or an equivalent like csrf_protect has not run.
# The view decorator requires_csrf_token can be used to ensure the template tag does work.
# This decorator works similarly to csrf_protect, but never rejects an incoming request.
#

#
# Example:
#

from django.shortcuts import render
from django.views.decorators.csrf import requires_csrf_token

@requires_csrf_token

def my_view(request):
c = {}

# ...

return render(request, "a_template.html", c)