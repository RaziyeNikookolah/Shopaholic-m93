



$(document).ready(function () {
    // Hide the H2 element initially
    $('#signup-div', '#code-verify-div').hide();

    // Listen for click event on the button
    $('#li_login').on('click', function () {
        // Toggle the H2 element's visibility on button click
        $('#signup-div').toggle();
    });
});
phone_number2 = $('#phone_number2')
// $('#login_btn').on('click', function () {
$(document).on('submit', '#login_form', function (e) {
    e.preventDefault();
    // let cookie = document.cookie
    // let csrfToken = cookie.substring(cookie.indexOf('=') + 1)

    $.ajax({

        url: 'otp/request_otp/',
        type: 'POST',
        // headers: {
        //     'X-CSRFToken': csrfToken
        // }
        data: {
            phone_number: $('#phone_number').val(),
            'csrfmiddlewaretoken': '{{csrf_token}}'
        },
        dataType: "json"

        // csrfmiddleware_token: $('input[name=csrfmiddleware_token]').val()
    }).then(res => {

        console.log(res);
    });
    $('#signup-div').hide();
    $('#code-verify-div').show();
    phone_number2.val($('#phone_number').val())

});
$(document).on('submit', '#code-verify_form', function (e) {
    e.preventDefault();
    // let cookie = document.cookie
    // let csrfToken = cookie.substring(cookie.indexOf('=') + 1)

    $.ajax({

        url: 'otp/verify_otp/',
        type: 'POST',
        // headers: {
        //     'X-CSRFToken': csrfToken
        // }
        data: {
            phone_number: $('#phone_number2').val(),
            code: $('#code').val(),
            'csrfmiddlewaretoken': '{{csrf_token}}'
        },
        dataType: "json"

        // csrfmiddleware_token: $('input[name=csrfmiddleware_token]').val()
    }).then(res => {

        console.log(res);
    });
    $('#signup-div').hide();
    $('#code-verify-div').hide();

});