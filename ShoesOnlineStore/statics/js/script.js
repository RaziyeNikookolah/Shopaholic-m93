
// let phone_number = '';
$(document).on('submit', '#login_form', function (e) {
    e.preventDefault();
    phone_number = $('#phone_number').val();
    next = $('#hidden_next').val();
    console.log(next)
    $.ajax({

        url: 'http://localhost:8000/otp/request_otp/',
        type: 'POST',
        data: {
            next: next,
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

    const url = window.location.href;
    // Split the URL by '/'
    const urlParts = url.split('/');

    // Retrieve the value of the path parameter from the appropriate index
    const pathParamValue = urlParts[6]; // Adjust the index based on your URL structure
    console.log(pathParamValue);

    $.ajax({

        url: 'http://localhost:8000/otp/verify_otp/',
        type: 'POST',
        data: {
            phone_number: phone_number,
            code: $('#code').val(),
            next: '/' + pathParamValue + '/',
            'csrfmiddlewaretoken': '{{csrf_token}}'
        },
        dataType: "json",
        success: function (res, status, xhr) {
            console.log(res);
            console.log("tokens and next must be here");
            window.location = 'http://127.0.0.1:8000/' + pathParamValue + '/';

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



