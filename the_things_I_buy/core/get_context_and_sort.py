def get_context_and_sort(list_products):
    context = {
        'meat': [prod for prod in list_products if prod.section.name == 'Meat'],
        'vegetables': [prod for prod in list_products if prod.section.name == 'Vegetables'],
        'fruits': [prod for prod in list_products if prod.section.name == 'Fruits'],
        'dairy': [prod for prod in list_products if prod.section.name == 'Dairy'],
        'drinks': [prod for prod in list_products if prod.section.name == 'Drinks'],
        'pasta': [prod for prod in list_products if prod.section.name == 'Pasta'],
        'alcohol': [prod for prod in list_products if prod.section.name == 'Alcohol'],
        'jars': [prod for prod in list_products if prod.section.name == 'Jars'],
        'cans': [prod for prod in list_products if prod.section.name == 'Cans'],
        'sea_food': [prod for prod in list_products if prod.section.name == 'Sea Food'],
        'sweets': [prod for prod in list_products if prod.section.name == 'Sweets'],
        'others_pantry': [prod for prod in list_products if prod.section.name == 'Others Pantry'],
        'others_fridge': [prod for prod in list_products if prod.section.name == 'Others Fridge'],
    }
    for key, value in context.items():
        context[key] = sorted(value, key=lambda x: x.name)
    return context