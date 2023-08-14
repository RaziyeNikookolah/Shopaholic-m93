$(document).ready(function () {
    $('#login_container').hide();

    $('#li_login').on('click', function () {
        $('#login_container',).toggle();
    });
});
function login() {
    $('#login_container',).show();
}
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
            console.log(status);
            console.log(res);
            // let formData = new FormData();
            // formData.append('phone_number', phone_number);
            // formData.append('password', '123');


            //  $.ajax({
            //     url: "http://localhost:8000/token/",
            //     type: "POST",
            //     data: formData,
            //     cache: false,
            //     processData: false,
            //     contentType: false,
            //     success: function (data) {
            //         window.localStorage.setItem('refreshToken', data['refresh']);
            //         window.localStorage.setItem('accessToken', data['access']);
            //         console.log(data['access']);
            //     },
            //     error: function (rs, e) {
            //         console.log("*************")
            //         console.error(rs.status);
            //         console.error(rs.responseText);
            //     }
            // }); // end ajax 

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



