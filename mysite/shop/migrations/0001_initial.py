# Generated by Django 5.0.4 on 2024-04-12 07:33

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=500)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('discount', models.IntegerField(default=0)),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
                ('is_archived', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_address', models.CharField(max_length=50)),
                ('promocode', models.CharField(default='', max_length=10)),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('products', models.ManyToManyField(related_name='order', to='shop.product')),
            ],
            options={
                'db_table': 'order',
            },
        ),
    ]
