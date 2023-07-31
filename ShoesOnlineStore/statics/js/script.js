



$(document).ready(function () {
    // Hide the H2 element initially
    $('#div-login').hide();

    // Listen for click event on the button
    $('#li_login').on('click', function () {
        // Toggle the H2 element's visibility on button click
        $('#div-login').toggle();
    });
});

$('#login_btn').on('click', function () {

    let cookie = document.cookie
    let csrfToken = cookie.substring(cookie.indexOf('=') + 1)

    $.ajax({
        url: 'accounts/get_phone_number/',
        type: 'POST',
        headers: {
            'X-CSRFToken': csrfToken
        }
    }).then(res => {

        console.log(res);
    });
});