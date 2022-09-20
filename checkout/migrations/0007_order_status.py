# Generated by Django 3.2 on 2022-09-20 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_order_user_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(0, 'Processing'), (1, 'Shipped'), (2, 'Completed'), (3, 'Hold'), (2, 'Cancelled')], default=0),
        ),
    ]
