# Generated by Django 4.1.1 on 2022-11-18 11:42

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reseller_app', '0008_product_p_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=12)),
                ('password', models.CharField(max_length=30)),
                ('address', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(default='', max_length=200)),
                ('quantity', models.IntegerField()),
                ('status', models.CharField(default='', max_length=20)),
                ('date', models.DateField(default=datetime.date(2022, 11, 18))),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
                ('productid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reseller_app.product')),
            ],
        ),
        migrations.CreateModel(
            name='AddCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(default=1)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reseller_app.product')),
            ],
        ),
    ]
