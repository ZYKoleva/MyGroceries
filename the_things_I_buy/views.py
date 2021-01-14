from django.http import JsonResponse
from django.shortcuts import render, redirect

from the_things_I_buy.core.add_default_products import add_default_products_to_user
from the_things_I_buy.core.clean_up_image import clean_up_image_file
from the_things_I_buy.core.generate_default_products import generate_default_product
from the_things_I_buy.core.remove_all_created_by_user_products import remove_all_created_by_user_products
from the_things_I_buy.forms import ProductForm
from the_things_I_buy.models import Product, MyProducts



def load_home(request):
    if request.user.is_authenticated:
        my_products_user = MyProducts.objects.filter(created_by=request.user)
        if len(my_products_user) == 0:
            context = add_default_products_to_user(request)
            return render(request, 'home.html', context)
        else:
            my_products_ids = [prod.user_product_id for prod in my_products_user]
            my_products = Product.objects.filter(pk__in=my_products_ids)
            context = {
                'meat': [prod for prod in my_products if prod.section.name == 'Meat'],
                'vegetables': [prod for prod in my_products if prod.section.name == 'Vegetables'],
                'fruits': [prod for prod in my_products if prod.section.name == 'Fruits'],
                'dairy': [prod for prod in my_products if prod.section.name == 'Dairy'],
                'drinks': [prod for prod in my_products if prod.section.name == 'Drinks'],
                'pasta': [prod for prod in my_products if prod.section.name == 'Pasta'],
                'alcohol': [prod for prod in my_products if prod.section.name == 'Alcohol'],
                'jars': [prod for prod in my_products if prod.section.name == 'Jars'],
                'cans': [prod for prod in my_products if prod.section.name == 'Cans'],
                'sea_food': [prod for prod in my_products if prod.section.name == 'Sea Food'],
                'others': [prod for prod in my_products if prod.section.name == 'Others'],
            }
            return render(request, 'home.html', context)

    else:
        context = generate_default_product()
        return render(request, 'home–default.html', context)


def add_product(request):
    if request.method == "GET":
        context = {
            'new_product': ProductForm()
        }
        return render(request, 'add_product.html', context)
    else:
        new_product = ProductForm(request.POST, request.FILES or None)
        if new_product.is_valid():
            my_product = new_product.save()
            my_product_user = MyProducts(created_by=request.user, user_product=my_product)
            my_product_user.save()
            return redirect('load home page')
        else:
            context = {
                'new_product': ProductForm(request.POST, request.FILES, instance=new_product)
            }
            return render(request, 'add_product.html', context)


def update_product(request, pk):
    prod_to_update = Product.objects.get(pk=pk)
    if request.method == "GET":
        context = {
            'product': ProductForm(instance=prod_to_update),
            'pk': pk
        }
        return render(request, 'update_product.html', context)
    else:
        product_form = ProductForm(request.POST, request.FILES or None, instance=prod_to_update)
        if product_form.is_valid():
            product_form.save()
            return redirect('load home page')
        else:
            context = {
                'product': product_form,
                'pk': pk
            }
            return render(request, 'update_product.html', context)


def remove_product(request, pk):
    prod_to_delete = Product.objects.get(pk=pk)
    my_products_user = MyProducts.objects.get(user_product_id = pk, created_by=request.user)
    my_products_user.delete()
    if prod_to_delete.customized_prod:
        prod_to_delete.delete()
    return redirect('load home page')


def save_product_changes(request):
    if request.is_ajax and request.method == "GET":
        products_ids_available = request.GET.get('products_ids_available').split(', ')[:-1]
        products_ids_unavailable = request.GET.get('products_ids_unavailable').split(', ')[:-1]
        products_available = Product.objects.filter(pk__in=products_ids_available)
        products_unavailable = Product.objects.filter(pk__in=products_ids_unavailable)
        for prod in products_available:
            if not prod.availability:
                prod.availability = True
                prod.save()
        for prod in products_unavailable:
            if prod.availability:
                prod.availability = False
                prod.save()
    return JsonResponse({"valid": False}, status=200)


def reset_default_settings(request):
    remove_all_created_by_user_products(request)
    return redirect('load home page')