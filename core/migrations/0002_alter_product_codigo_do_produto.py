# Generated by Django 4.1 on 2022-08-28 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="codigo_do_produto",
            field=models.IntegerField(verbose_name="Codigo de produto"),
        ),
    ]
