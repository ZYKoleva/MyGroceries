from django.contrib import admin

# Register your models here.
from the_things_I_buy.models import Product, MyProducts, Section

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'customized_prod', 'availability')


class MyProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_by', 'user_product')


admin.site.register(Product, ProductAdmin)
admin.site.register(MyProducts, MyProductsAdmin)
admin.site.register(Section)

