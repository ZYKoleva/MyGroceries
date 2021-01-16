from the_things_I_buy.core.get_context_and_sort import get_context_and_sort
from the_things_I_buy.models import Product, MyProducts


def add_default_products_to_user(request):
    default_products_list = Product.objects.filter(customized_prod=False)
    for prod in default_products_list:
        my_prod = Product(name=prod.name, brand=prod.brand, img=prod.img, section=prod.section, customized_prod=True)
        my_prod.save()
        my_products_user = MyProducts(created_by=request.user, user_product=my_prod)
        my_products_user.save()
    my_products_user = MyProducts.objects.filter(created_by=request.user)
    my_products_ids = [prod.user_product_id for prod in my_products_user]
    my_products = Product.objects.filter(pk__in=my_products_ids)
    context = get_context_and_sort(my_products)
    return context
