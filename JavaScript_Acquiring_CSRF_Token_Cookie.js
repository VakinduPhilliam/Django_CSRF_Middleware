/* Acquiring CSRF Token Cookie. */
/*
Acquiring the token if CSRF_USE_SESSIONS and CSRF_COOKIE_HTTPONLY are False.
The recommended source for the token is the csrftoken cookie, which will be set if you’ve enabled CSRF protection for your views as outlined above.
The CSRF token cookie is named csrftoken by default, but you can control the cookie name via the CSRF_COOKIE_NAME setting.
Acquiring the token is straightforward:
*/

function getCookie(name) {

var cookieValue = null;

if (document.cookie && document.cookie !== '') {

var cookies = document.cookie.split(';');

for (var i = 0; i < cookies.length; i++) {
var cookie = cookies[i].trim();

// Does this cookie string begin with the name we want?

if (cookie.substring(0, name.length + 1) === (name + '=')) {

cookieValue = decodeURIComponent(cookie.substring(name.length + 1));

break;

       }

   }

}

return cookieValue;

}

var csrftoken = getCookie('csrftoken');

/* The above code could be simplified by using the JavaScript Cookie library to replace getCookie: */

var csrftoken = Cookies.get('csrftoken');

/*
Note: The CSRF token is also present in the DOM, but only if explicitly included using csrf_token in a template.
The cookie contains the canonical token; the CsrfViewMiddleware will prefer the cookie to the token in theDOM. 
Regardless, you’re guaranteed to have the cookie if the token is present in the DOM, so you should use the cookie!
*/