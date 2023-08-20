accessToken = window.localStorage.getItem('accessToken');
refreshToken = window.localStorage.getItem('refreshToken');
if (accessToken) {
    console.log("access exists")
    fetch('http://localhost:8000/checkout/', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            "Authorization": "Bearer " + accessToken,
        },
    })
        .then(response => {
            console.log(response);

            if (response.status == 401) {
                console.log(401, "access token expired");

                fetch('http://localhost:8000/checkout/', {
                    method: 'GET',
                    headers: {
                        'Content-Type': 'application/json',
                        "Authorization": "Bearer " + refreshToken,
                    },
                })
                    .then(response => {
                        console.log(response);
                        if (response.status == 401) {
                            console.log(401, "refresh token expired");
                            window.location = 'http://127.0.0.1:8000/api/v1/accounts/optain_pair_tokens/?next=/checkout/';
                        }
                        else {
                            console.log("received new access and refresh tokens using last refresh token");

                            window.localStorage.setItem('refreshToken', response['refresh_token']);
                            window.localStorage.setItem('accessToken', response['access_token']);
                        }
                    })

                    .catch(error => {
                        console.error('Error:', error);
                    });
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
}
else {
    window.location = 'http://127.0.0.1:8000/accounts/login/?next=/checkout/';
    console.log("access token not exists");

}