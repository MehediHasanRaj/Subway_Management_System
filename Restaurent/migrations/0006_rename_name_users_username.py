# Generated by Django 4.2.4 on 2023-08-31 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurent', '0005_alter_menuitems_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='name',
            new_name='username',
        ),
    ]