from the_things_I_buy.models import Product


def generate_default_product():
    default_products_list = Product.objects.filter(customized_prod=False)

    context = {
        'meat': [prod for prod in default_products_list if prod.section.name == 'Meat'],
        'vegetables': [prod for prod in default_products_list if prod.section.name == 'Vegetables'],
        'fruits': [prod for prod in default_products_list if prod.section.name == 'Fruits'],
        'dairy': [prod for prod in default_products_list if prod.section.name == 'Dairy'],
        'pasta': [prod for prod in default_products_list if prod.section.name == 'Pasta'],
        'alcohol': [prod for prod in default_products_list if prod.section.name == 'Alcohol'],
        'jars': [prod for prod in default_products_list if prod.section.name == 'Jars'],
        'cans': [prod for prod in default_products_list if prod.section.name == 'Cans'],
        'sea_food': [prod for prod in default_products_list if prod.section.name == 'Sea Food'],
        'sweets': [prod for prod in default_products_list if prod.section.name == 'Sweets'],
        'others': [prod for prod in default_products_list if prod.section.name == 'Others'],
    }
    return context
