# Generated by Django 3.1.5 on 2021-01-12 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('the_things_I_buy', '0004_product_customized_prod'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='producer',
            new_name='brand',
        ),
    ]
