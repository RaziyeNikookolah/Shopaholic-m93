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

    // Define a function to load data for the given URL
    function loadPageData(url) {
        $.ajax({
            url: url,
            type: 'GET',
            dataType: 'json',
            beforeSend: function (xhr) {
                xhr.setRequestHeader('Authorization', 'Bearer ' + accessToken);
            },
            success: function (data) {
                let output = '<div class="row mb-5" id="all_products">';
                data.results.forEach((element) => {
                    // Your existing code to generate the product card HTML
                    output += '<div class="col-sm-6 col-lg-4 mb-4" data-aos="fade-up" >' +
                        '<div class="block-4 text-center border">' +
                        '<figure class="block-4-image">' +
                        ' <a href=""><img src="' + element.image + '"  alt="Image placeholder" class="img-fluid"></a>' +
                        '</figure>' +
                        '<div class="block-4-text p-4">' +
                        '<h3 "><a  href="/shop_single/' + element.id + '/">' + element.brand + '</a></h3>' +
                        '<h5>' + element.category + '</h5>' +
                        '<p class="mb-0">' + element.descriptions + '</p>' +
                        '<p class="text-primary font-weight-bold">$' + element.last_price + '</p>' +
                        '</div>' +
                        '</div>' +
                        '</div>';

                });
                output += '</div>';
                $('#all_products').html(output);

                // Update the "Next" and "Previous" button URLs
                $('#next_page').attr('href', data.next); // Update this line with the correct path
                $('#previuse_page').attr('href', data.previous); // Update this line with the correct path
            },
            error: function (jqXhr, textStatus, errorMessage) {
                console.log('Error in loading data', errorMessage);
            },
        });
    }

    // Initial load of the first page
    loadPageData('http://localhost:8000/shoes/product_list/');


    // Add an event listener for the "Next" button
    $('#next_page').on('click', function (e) {
        e.preventDefault();

        // Extract the URL for the next page from the "Next" button's href attribute
        const nextPageUrl = $(this).attr('href');

        // Load the data for the next page
        loadPageData(nextPageUrl);
    });

    // Add an event listener for the "Previous" button
    $('#previuse_page').on('click', function (e) {
        e.preventDefault();

        // Extract the URL for the previous page from the "Previous" button's href attribute
        const prevPageUrl = $(this).attr('href');

        // Load the data for the previous page
        loadPageData(prevPageUrl);
    });


    $('#search_form').on('keypress', function (e) {
        if (e.keyCode == 13) {
            e.preventDefault();
            const accessToken = window.localStorage.getItem('accessToken');
            loadPageData('http://127.0.0.1:8000/shoes/product_list/?search=' + $('#search_form').val());

        }

    });

    function bootstrapColor(color) {

        switch (color.toLowerCase()) {
            case 'blue':
            case 'darkBlue':
                return 'bg-primary';
            case 'gray':
                return 'bg-secondary';
            case 'green':
                return 'bg-success';
            case 'red':
                return 'bg-danger';
            case 'yellow':
                return 'bg-warning';
            case 'lightBlue':
                return 'bg-info';
            case 'light':
                return 'bg-light';
            case 'black':
                return 'bg-dark';
            case 'white':
                return 'bg-white';
            case 'purple':
                return 'bg-purple'
            default:
                return '';
        }

    }

    $("#slider-range").slider({
        range: true,
        min: 0,
        max: 1000,  // Adjust the maximum value based on your actual data
        values: [0, 1000],  // Adjust initial values as needed
        slide: function (event, ui) {
            $("#amount").val("$" + ui.values[0] + " - $" + ui.values[1]);
        },
        stop: function (event, ui) {
            // Extract selected price range
            var minPrice = ui.values[0];
            var maxPrice = ui.values[1];

            // Send a request to the server to filter products by price range
            var url = "http://localhost:8000/shoes/product_list/?min_price=" + minPrice + "&max_price=" + maxPrice;
            loadPageData(url);
        }
    });


    var div_color = $('#colors');

    function getColors() {
        var div_color = $('#colors');
        const accessToken = window.localStorage.getItem('accessToken');
        $.ajax({
            url: 'http://127.0.0.1:8000/api/v1/shoes/colors/',
            type: 'GET',
            dataType: 'json',
            beforeSend: function (xhr) {
                xhr.setRequestHeader("Authorization", "Bearer " + accessToken);
            },
            success: function (response) {
                var output = '<h3 class="mb-3 h6 text-uppercase text-black d-block">Color</h3>';
                for (var colorKey in response) {
                    var color = response[colorKey];

                    output += '<a href="#" class="d-flex color-item align-items-center" id="color_' + color.id + '">' +
                        '<span class="' + bootstrapColor(color.name) + ' color d-inline-block rounded-circle mr-2"></span> <span class="text-black">' + color.name + '</span>' +
                        '</a>';
                }
                div_color.html(output);

                // Attach click event using jQuery
                $('[id^="color_"]').on('click', function () {
                    var colorText = $(this).find('span:last-child').text();
                    console.log('Clicked Color:', colorText);

                    loadPageData('http://127.0.0.1:8000/shoes/product_list/?title=&category__title=&brand__title=&size__number=&color__name=' + colorText);
                });
            },
            error: function (error) {
                console.error('Error:', error);
            }
        });
    }
    getColors();

    getCategories();
    var ul = $('#ulCategories');
    function getCategories() {
        var output = '<ul class="list-unstyled mb-0" id="ulCategories">';
        var ul = $('#ulCategories');  // Store the ul element in a variable
        const accessToken = window.localStorage.getItem('accessToken');
        $.ajax({
            url: 'http://127.0.0.1:8000/api/v1/shoes/categories/',
            type: 'GET',
            dataType: 'json',
            beforeSend: function (xhr) {
                xhr.setRequestHeader("Authorization", "Bearer " + accessToken);
            },
            success: function (response) {
                for (var categoryKey in response) {
                    var category = response[categoryKey];

                    output += '<li class="mb-1" id="category_' + categoryKey + '"><a href="#" class="d-flex"><span>' + category.title + '</span> <span class="text-black ml-auto">(2,220)</span></a></li>';
                }
                output += '</ul>';
                ul.html(output);

                // Attach click event using jQuery
                $('[id^="category_"]').on('click', function () {
                    var categoryText = $(this).find('span:first-child').text();
                    console.log('Clicked Category:', categoryText);

                    loadPageData('http://localhost:8000/shoes/product_list/?category__title=' + categoryText);
                });
            },
            error: function (error) {
                console.error('Error:', error);
            }
        });
    }


});