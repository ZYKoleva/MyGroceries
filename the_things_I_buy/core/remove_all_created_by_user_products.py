from the_things_I_buy.models import Product, MyProducts


def remove_all_created_by_user_products(request):
    my_products_user = MyProducts.objects.filter(created_by=request.user)
    my_products_ids = [prod.user_product_id for prod in my_products_user]
    my_products = Product.objects.filter(pk__in=my_products_ids)
    for prod in my_products:
        prod.delete()

