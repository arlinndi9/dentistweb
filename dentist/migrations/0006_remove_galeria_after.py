# Generated by Django 4.0.5 on 2022-06-15 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dentist', '0005_galeria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='galeria',
            name='after',
        ),
    ]
