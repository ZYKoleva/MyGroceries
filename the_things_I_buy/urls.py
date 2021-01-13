from django.urls import path

from the_things_I_buy.views import load_home, add_product, update_product, remove_product, save_product_changes, \
    reset_default_settings

urlpatterns = [
    path('', load_home, name = 'load home page'),
    path('add_product/', add_product, name = 'add product'),
    path('update_product/<int:pk>/', update_product, name = 'update product'),
    path('remove_product/<int:pk>/', remove_product, name = 'remove product'),
    path('get/ajax/save-product-changes/', save_product_changes, name = 'save product changes'),
    path('reset_default_settings/', reset_default_settings, name = 'reset default')
]