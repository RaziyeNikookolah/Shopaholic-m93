$(document).ready(function () {

    $.ajax({
        url: 'http://localhost:8000/shoes/product_list/',
        type: 'GET',
        dataType: "json",
        success: function (data, status, xhr) {

            output = '<div class="row mb-5" id="all_products">'
            data.forEach((element, index) => {
                // console.log(`Element ${index}:`, element);
                output += '<div class="col-sm-6 col-lg-4 mb-4" data-aos="fade-up" >' +
                    '<div class="block-4 text-center border">' +
                    '<figure class="block-4-image">' +
                    ' <a href=""><img src="' + element.image + '"  alt="Image placeholder" class="img-fluid"></a>' +
                    '</figure>' +
                    '<div class="block-4-text p-4">' +
                    '<h3 "><a  href="/shop_single/' + element.id + '/">' + element.brand + '</a></h3>' +
                    '<p class="mb-0">' + element.descriptions + '</p>' +
                    '<p class="text-primary font-weight-bold">$' + element.last_price + '</p>' +
                    '</div>' +
                    '</div>' +
                    '</div>';
            });
            output += '</div>';
            $('#all_products').html(output);


        },
        error: function (jqXhr, textStatus, errorMessage) { // error callback 
            console.log('Error in loading data', errorMessage);
        },
    });

    $('#search_form').on('keypress', function (e) {

        if (e.keyCode == 13) {
            e.preventDefault();

            $.ajax({
                url: 'http://127.0.0.1:8000/shoes/product_list/?search=' + $('#search_form').val(),
                type: 'GET',
                dataType: "json",
                success: function (data, status, xhr) {

                    output = '<div class="row mb-5" >'
                    data.forEach((element, index) => {
                        // console.log(`Element ${index}:`, element);
                        output += '<div class="col-sm-6 col-lg-4 mb-4" data-aos="fade-up">' +
                            '<div class="block-4 text-center border">' +
                            '<figure class="block-4-image">' +
                            ' <a href=""><img src="' + element.image + '"  alt="Image placeholder" class="img-fluid"></a>' +
                            '</figure>' +
                            '<div class="block-4-text p-4">' +
                            '<h3 "><a  href="/shop_single/' + element.id + '/">' + element.brand + '</a></h3>' +
                            '<p class="mb-0">' + element.descriptions + '</p>' +
                            '<p class="text-primary font-weight-bold">$' + element.price + '</p>' +
                            '</div>' +
                            '</div>' +
                            '</div>';
                    });
                    output += '</div>';
                    $('#all_products').html(output);
                    // window.location = 'http://127.0.0.1:8000';

                },
                error: function (jqXhr, textStatus, errorMessage) { // error callback 
                    console.log('Error in loading data', errorMessage);
                },
            });
        }

    });
    getCategories();
    var ul = $('#ulCategories');
    function getCategories() {
        var output = '<ul class="list-unstyled mb-0" id="ulCategories">';
        var ul = $('#ulCategories');  // Store the ul element in a variable

        $.ajax({
            url: 'http://127.0.0.1:8000/api/v1/shoes/categories/',
            type: 'GET',
            dataType: 'json',
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
                });
            },
            error: function (error) {
                console.error('Error:', error);
            }
        });
    }


});