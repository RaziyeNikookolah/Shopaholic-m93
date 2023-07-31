



$(document).ready(function () {
    // Hide the H2 element initially
    $('#div-login').hide();

    // Listen for click event on the button
    $('#li_login').on('click', function () {
        // Toggle the H2 element's visibility on button click
        $('#div-login').toggle();
    });
});
