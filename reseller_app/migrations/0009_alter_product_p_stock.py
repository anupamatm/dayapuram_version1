# Generated by Django 4.1.2 on 2022-12-29 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reseller_app', '0008_product_p_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='p_stock',
            field=models.FloatField(default=0),
        ),
    ]