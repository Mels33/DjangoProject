# Generated by Django 5.0.4 on 2024-04-23 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]