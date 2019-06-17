# Python Cross Site Request Forgery protection (CSRF Protection) with Django
# The CSRF middleware and template tag provides easy-to-use protection against Cross Site Request Forgeries. 
# This type of attack occurs when a malicious website contains a link, a form button or some JavaScript that is intended to
# perform some action on your website, using the credentials of a logged-in user who visits the malicious site in their
# browser. 
# The first defense against CSRF attacks is to ensure that GET requests (and other ‘safe’ methods, as defined by RFC) are side effect free.
#

#
# View needs protection for one path.
# A view needs CSRF protection under one set of conditions only, and mustn’t have it for the rest of the time.
#
# Solution: use csrf_exempt() for the whole view function, and csrf_protect() for the path within it that needs protection.
#

#
# Example:
#

from django.views.decorators.csrf import csrf_exempt, csrf_protect

@csrf_exempt
def my_view(request):

@csrf_protect

def protected_path(request):
do_something()

if some_condition():
return protected_path(request)

else:

do_something_else()