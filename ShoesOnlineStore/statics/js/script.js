
// let phone_number = '';
$(document).on('submit', '#login_form', function (e) {
    e.preventDefault();
    phone_number = $('#phone_number').val();
    const data = {
        "phone_number": phone_number,
    };
    $.ajax({

        url: 'http://localhost:8000/otp/request_otp/',
        type: 'POST',

        contentType: 'application/json',
        data: JSON.stringify(data),
        success: function (data, status, xhr) {
            console.log(status);
        },
        error: function (jqXhr, textStatus, errorMessage) { // error callback 
            console.log('Error in login_form submission:', errorMessage);
            if (errorMessage == 'Bad Request') {
                $('#phone_number').val("");
            }
            else if (errorMessage == 'Internal Server Error') {
                $('#signup-div').hide();
                $('#code-verify-div').show();
            }
        }
    });


});


$(document).on('submit', '#code-verify_form', function (e) {
    e.preventDefault();



    const url = window.location.href;
    // Split the URL by '/'
    const urlParts = url.split('next=');
    console.log(urlParts);

    const data = {
        "phone_number": phone_number,
        "code": $('#code').val()
    };
    $.ajax({

        url: 'http://localhost:8000/otp/verify_otp/',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify(data),
        success: function (res, status, xhr) {


            window.localStorage.setItem('refreshToken', res['refresh_token']);
            window.localStorage.setItem('accessToken', res['access_token']);
            if (urlParts[1]) {
                window.location = 'http://127.0.0.1:8000/' + urlParts[1];
            } else {
                window.location = 'http://127.0.0.1:8000/';
            }
        },
        error: function (jqXhr, textStatus, errorMessage) {
            console.log(textStatus);//open login form and take next redirect
            console.log('Error in code-verify_form submission:', errorMessage);
        }
    });
    $('#signup-div').hide();
    $('#code-verify-div').hide();
    $('#login_container').hide();
    $('#phone_number').val("")
    $('#code').val("")

});






// $(document).on('click', '#logout_btn', function (e) {
//     const accessToken = window.localStorage.getItem('accessToken');

//     e.preventDefault();
//     var nextUrl = '';
//     $.ajax({
//         url: 'http://localhost:8000/accounts/request_logout/',
//         type: 'GET',
//         beforeSend: function (xhr) {
//             xhr.setRequestHeader("Authorization", "Bearer " + accessToken);
//         },
//         success: function (res, status, xhr) {
//             console.log("logged out successfully..");
//             window.localStorage.removeItem('accessToken')
//             window.localStorage.removeItem('refreshToken')

//         },
//         error: function (jqXhr, textStatus, errorMessage) {
//             console.log(textStatus);

//         }
//     });

//     window.location = 'http://127.0.0.1:8000/accounts/login/?next=' + nextUrl;
// });