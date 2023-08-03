$(document).ready(function () {

    $.ajax({
        url: 'shoes/product_list/',
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
                    '<h3 "><a  href="/shop_single/' + element.id + '">' + element.brand + '</a></h3>' +
                    '<p class="mb-0">' + element.descriptions + '</p>' +
                    '<p class="text-primary font-weight-bold">$' + element.price + '</p>' +
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
            // alert('You pressed enter!');
            // }
            $.ajax({
                url: 'shoes/search_list/',
                type: 'GET',
                data: { search: $('#search_form').val() },
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
                            '<h3 class="product"><a href="">' + element.brand + '</a></h3>' +
                            '<p class="mb-0">' + element.descriptions + '</p>' +
                            '<p class="text-primary font-weight-bold">$' + element.price + '</p>' +
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
        }

    });
    // search_list/


});
function go_to_single_shop() {

    Window.location.replace("http://www.google.com");
    console.log("go.......")
}