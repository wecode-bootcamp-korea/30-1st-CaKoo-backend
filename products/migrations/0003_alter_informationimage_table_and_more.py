# Generated by Django 4.0.2 on 2022-03-02 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_sizes'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='informationimage',
            table='information_images',
        ),
        migrations.AlterModelTable(
            name='productimage',
            table='product_images',
        ),
        migrations.AlterModelTable(
            name='productsize',
            table='product_sizes',
        ),
    ]
