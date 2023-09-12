$(document).ready(function () {
    const accessToken = window.localStorage.getItem('accessToken');
    const liLoginSpan = $("#li_login span");

    if (accessToken) {
        liLoginSpan.find('i').removeClass('bi bi-arrow-right-square');
        liLoginSpan.find('i').addClass("bi bi-person-fill");
        liLoginSpan.html('<i class="bi bi-person-fill"></i>'); // Change span content
    } else {
        liLoginSpan.find('i').removeClass('bi bi-person-fill');
        liLoginSpan.find('i').addClass("bi bi-arrow-right-square");
        liLoginSpan.html('LOGIN <i class="bi bi-arrow-right-square"></i>'); // Change span content
    }



    function loadNewPage(url, nextUrl) {
        const accessToken = window.localStorage.getItem('accessToken');
        // Add the nextUrl parameter to the URL if provided
        if (nextUrl) {
            url += (url.includes('?') ? '&' : '?') + 'next=' + nextUrl;
        }

        fetch(url, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                "Authorization": "Bearer " + accessToken,
            },
        })
            .then(response => response.text())
            .then(html => {
                // Replace the current document's content with the content of the new page
                document.open();
                document.write(html);
                document.close();
            })
            .catch(error => {
                console.error('Error loading page:', error);
            });
    }

});