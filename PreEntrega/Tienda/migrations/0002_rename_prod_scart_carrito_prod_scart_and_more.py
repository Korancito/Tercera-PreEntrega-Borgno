# Generated by Django 5.0.3 on 2024-03-30 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carrito',
            old_name='Prod_SCart',
            new_name='Prod_Scart',
        ),
        migrations.RenameField(
            model_name='productos',
            old_name='Prod_Sale',
            new_name='Prod_sale',
        ),
    ]
