# Python Clickjacking Protection with Django.
# The clickjacking middleware and decorators provide easy-to-use protection against clickjacking.
# This type of attack occurs when a malicious site tricks a user into clicking on a concealed element of another site which they have loaded
# in a hidden frame or iframe.
#

#
# Setting X-Frame-Options per view:
# To set the X-Frame-Options header on a per view basis, Django provides these decorators:
#

from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_deny
from django.views.decorators.clickjacking import xframe_options_sameorigin

@xframe_options_deny

def view_one(request):

return HttpResponse("I won't display in any frame!")

@xframe_options_sameorigin

def view_two(request):

return HttpResponse("Display in a frame if it's from the same origin as me.")
