

$(document).ready(function () {
    const accessToken = window.localStorage.getItem('accessToken');
    if (accessToken) {
        console.log("access token is here");
        showLiElement(); // Show logout element
        hideLiLogin();  // Hide login element
    } else {
        console.log("access token is not here");

        showLiLogin();   // Show login element
        hideLiElement(); // Hide logout element
    }
});
// Get the li element by its ID
const liLogin = document.getElementById('li_login');

// Show the li element
function showLiLogin() {
    liLogin.style.display = 'block';
}

// Hide the li element
function hideLiLogin() {
    liLogin.style.display = 'none';
}

const liLogout = document.getElementById('li_logout');

// Show the li element
function showLiElement() {
    liLogout.style.display = 'block';
}

// Hide the li element
function hideLiElement() {
    liLogout.style.display = 'none';
}





liLogin.addEventListener('click', function () {

    const nextUrl = 'http://127.0.0.1:8000';  // Replace with the actual URL

    window.location = 'http://127.0.0.1:8000/accounts/login/?next=' + nextUrl;

});

// const menu_item_logout = document.getElementById('menu_item_logout');
// menu_item_logout.addEventListener('click', function () {

//     hideLiElement(); // Hide logout element
//     showLiLogin();   // Show login element
//     window.location = 'http://127.0.0.1:8000/accounts/logout/?next=/';

// });

// const menu_item_profile = document.getElementById('menu_item_profile');
// liLogout.addEventListener('click', function () {

//     window.location = 'http://127.0.0.1:8000/accounts/profile/'; // it should send account id

// });

