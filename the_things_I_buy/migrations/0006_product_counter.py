# Generated by Django 3.1.5 on 2021-01-24 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('the_things_I_buy', '0005_auto_20210112_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='counter',
            field=models.IntegerField(default=1),
        ),
    ]