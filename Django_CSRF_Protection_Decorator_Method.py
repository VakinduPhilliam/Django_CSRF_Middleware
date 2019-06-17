# Python Cross Site Request Forgery protection (CSRF Protection) with Django
# The CSRF middleware and template tag provides easy-to-use protection against Cross Site Request Forgeries. 
# This type of attack occurs when a malicious website contains a link, a form button or some JavaScript that is intended to
# perform some action on your website, using the credentials of a logged-in user who visits the malicious site in their
# browser. 
# The first defense against CSRF attacks is to ensure that GET requests (and other ‘safe’ methods, as defined by RFC) are side effect free.
#

#
# The decorator method:
# Rather than adding CsrfViewMiddleware as a blanket protection, you can use the csrf_protect decorator,
# which has exactly the same functionality, on particular views that need the protection. It must be used both on views
# that insert the CSRF token in the output, and on those that accept the POST form data. (These are often the same view function, but not always).
# Use of the decorator by itself is not recommended, since if you forget to use it, you will have a security hole. 
# The ‘belt and braces’ strategy of using both is fine, and will incur minimal overhead.
#

#
# csrf_protect(view)
# Decorator that provides the protection of CsrfViewMiddleware to a view.
#

#
# Usage:
#

from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

@csrf_protect

def my_view(request):
c = {}

# ...

return render(request, "a_template.html", c)
