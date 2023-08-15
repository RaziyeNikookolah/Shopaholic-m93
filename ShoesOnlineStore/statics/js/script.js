
let phone_number = '';
$(document).on('submit', '#login_form', function (e) {
    e.preventDefault();
    phone_number = $('#phone_number').val();
    $.ajax({

        url: 'http://localhost:8000/otp/request_otp/',
        type: 'POST',
        data: {
            phone_number: phone_number,
            'csrfmiddlewaretoken': '{{csrf_token}}'
        },
        dataType: "json",
        success: function (data, status, xhr) {
            console.log(status);
        },
        error: function (jqXhr, textStatus, errorMessage) { // error callback 
            console.log('Error in login_form submission:', errorMessage);
        },
    });
    $('#signup-div').hide();
    $('#code-verify-div').show();

});
$(document).on('submit', '#code-verify_form', function (e) {
    e.preventDefault();

    $.ajax({

        url: 'http://localhost:8000/otp/verify_otp/',
        type: 'POST',
        data: {
            phone_number: phone_number,
            code: $('#code').val(),
            'csrfmiddlewaretoken': '{{csrf_token}}'
        },
        dataType: "json",
        success: function (res, status, xhr) {
            window.localStorage.setItem('refreshToken', res['refresh_token']);
            window.localStorage.setItem('accessToken', res['access_token']);
            //console.log(window.localStorage.getItem('refreshToken'));
        },
        error: function (jqXhr, textStatus, errorMessage) {
            console.log('Error in code-verify_form submission:', errorMessage);
        }
    });
    $('#signup-div').hide();
    $('#code-verify-div').hide();
    $('#login_container').hide();
    $('#phone_number').val("")
    $('#code').val("")

});



