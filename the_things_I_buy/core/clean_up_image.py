import os


def clean_up_image_file(product):
    product_image = product.img
    if product_image:
        os.remove(product_image.path)