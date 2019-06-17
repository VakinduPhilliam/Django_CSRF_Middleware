# Python Clickjacking Protection with Django.
# The clickjacking middleware and decorators provide easy-to-use protection against clickjacking.
# This type of attack occurs when a malicious site tricks a user into clicking on a concealed element of another site which they have loaded
# in a hidden frame or iframe.
#

#
# View Decorator:
#
# When using the middleware there may be some views where you do not want the X-Frame-Options header set.
# For those cases, you can use a view decorator that tells the middleware not to set the header:
#

from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt

@xframe_options_exempt

def ok_to_load_in_a_frame(request):

return HttpResponse("This page is safe to load in a frame on any site.")
