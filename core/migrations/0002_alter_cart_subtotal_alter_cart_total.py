# Generated by Django 4.1 on 2022-11-26 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='subtotal',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=65, null=True),
        ),
    ]
