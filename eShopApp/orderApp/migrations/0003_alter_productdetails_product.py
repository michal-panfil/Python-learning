# Generated by Django 4.2.7 on 2023-11-06 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orderApp', '0002_remove_product_create_date_product_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetails',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='orderApp.product'),
        ),
    ]