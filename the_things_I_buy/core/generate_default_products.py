from the_things_I_buy.core.get_context_and_sort import get_context_and_sort
from the_things_I_buy.models import Product


def generate_default_product():
    default_products_list = Product.objects.filter(customized_prod=False)

    context = get_context_and_sort(default_products_list)
    return context
