# Generated by Django 4.2.4 on 2023-08-21 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurent', '0002_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='address',
            field=models.TextField(max_length=30),
        ),
    ]
