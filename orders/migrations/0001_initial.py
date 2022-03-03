# Generated by Django 4.0.2 on 2022-03-02 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0002_product_sizes'),
        ('users', '0003_alter_user_birthdate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=10, unique=True)),
                ('sender_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=500)),
                ('recipient_name', models.CharField(max_length=50)),
                ('recipient_phone', models.CharField(max_length=50)),
                ('ordered_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'orders',
            },
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'orderstatus',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderitems', to='orders.order')),
                ('product_size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderitems', to='products.productsize')),
            ],
            options={
                'db_table': 'orderitems',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='orders.orderstatus'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='users.user'),
        ),
    ]