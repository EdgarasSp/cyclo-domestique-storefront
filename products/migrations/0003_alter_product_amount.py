# Generated by Django 3.2 on 2022-09-14 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='amount',
            field=models.DecimalField(decimal_places=0, default=10, max_digits=10),
        ),
    ]
