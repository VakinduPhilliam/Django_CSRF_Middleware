# Django HTTP Provider
# If you’re using AngularJS 1.1.3 and newer, it’s sufficient to configure the $http provider with the cookie and header names:
#

# $httpProvider.defaults.xsrfCookieName = 'csrftoken';
# $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

#
# Using CSRF in Jinja2 templates
# Django’s Jinja2 template backend adds {{ csrf_input }} to the context of all templates which is equivalent
# to {% csrf_token %} in the Django template language. 
#

#
# For example:
#


# <form method="post">{{ csrf_input }}