# Generated by Django 4.0.5 on 2022-06-03 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='drink',
            old_name='name',
            new_name='drink_name',
        ),
    ]