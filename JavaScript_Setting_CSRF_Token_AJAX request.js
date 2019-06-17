/* JavaScript Setting the token on the AJAX request. */
/* 
You’ll have to actually set the header on your AJAX request, while protecting the CSRF token from being sent to other domains using
 settings.crossDomain in jQuery 1.5.1 and newer: 
*/

function csrfSafeMethod(method) {

// these HTTP methods do not require CSRF protection

return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));

}

$.ajaxSetup({

beforeSend: function(xhr, settings) {

if (!csrfSafeMethod(settings.type) && !this.crossDomain) {

xhr.setRequestHeader("X-CSRFToken", csrftoken);

    }
   }
});
