



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
        dataType: "json",
        success: function (data, status, xhr) {   // success callback function
            // $('p').append(data.firstName + ' ' + data.middleName + ' ' + data.lastName);
            console.log(status);
        },
        error: function (jqXhr, textStatus, errorMessage) { // error callback 
            console.log('Error in login_form submission:', errorMessage);
            // $('p').append('Error: ' + errorMessage);
        },


    });
    $('#signup-div').hide();
    $('#code-verify-div').show();
    phone_number2.val($('#phone_number').val())
    $('#phone_number').val("")
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
        dataType: "json",
        success: function (data, status, xhr) {
            console.log(status);

            // $.ajax({

            //     url: 'token/',
            //     type: 'POST',
            //     data: {
            //         grant_type: 'password',
            //         phone_number: $('#phone_number2').val(),
            //         'csrfmiddlewaretoken': '{{csrf_token}}',
            //         password: "123",
            //     },
            //     dataType: "json",
            //     headers: {
            //         'Content-Type': 'application/x-www-form-urlencoded'   // Set the appropriate content type
            //     },
            //     success: function (data, status, xhr) {   // success callback function
            //         console.log(data);
            //     },
            //     error: function (jqXhr, textStatus, errorMessage) { // error callback 
            //         console.log('Error in token request:', errorMessage);
            //     },
            // });







            let formData = new FormData();
            formData.append('phone_number', '09177302137');
            formData.append('password', '123');

            $.ajax({
                url: "token/",
                type: "POST",
                data: formData,
                cache: false,
                processData: false,
                contentType: false,
                success: function (data) {
                    // store tokens in localStorage
                    window.localStorage.setItem('refreshToken', data['refresh']);
                    window.localStorage.setItem('accessToken', data['access']);
                    console.log(data['access']);
                },
                error: function (rs, e) {
                    console.error(rs.status);
                    console.error(rs.responseText);
                }
            }); // end ajax










        },
        error: function (jqXhr, textStatus, errorMessage) {
            console.log('Error in code-verify_form submission:', errorMessage);
        }
    });
    $('#signup-div').hide();
    $('#code-verify-div').hide();
    $('#phone_number2').val("")
    $('#code').val("")

});