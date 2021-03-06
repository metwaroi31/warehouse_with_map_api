# Generated by Django 3.2.8 on 2021-12-09 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse_map_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='order_product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
                ('qty', models.DecimalField(decimal_places=0, max_digits=1000)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='warehouse_map_api.product')),
            ],
        ),
    ]
