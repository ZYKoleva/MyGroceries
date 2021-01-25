$('.save-product-changes').click(function(e) {
    e.preventDefault()
    const images = $('.modified-availability > img')
    const modifiedQuantityItems = $('.modified-quantity')
    let dict_modified_items = {}
    for (const item of modifiedQuantityItems){
        dict_modified_items[item.id] = item.textContent
    }
    let products_ids_available = ''
    let products_ids_unavailable = ''

    for (const prod of images) {
        if (prod.className === 'True') {
            products_ids_available += prod.id + ', '
        } else {
            products_ids_unavailable += prod.id + ', '
        }
    }

    $.ajax(
        {
            type: 'GET',
            url: "get/ajax/save-product-changes",
            data: {
                'products_ids_available': products_ids_available,
                'products_ids_unavailable': products_ids_unavailable,
                'dict_modified_items': JSON.stringify(dict_modified_items)
            },
            dataType: "json",
            success: function (response) {
                window.location = '';
            }
        }
    )
});
