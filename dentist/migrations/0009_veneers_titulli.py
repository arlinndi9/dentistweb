# Generated by Django 4.0.5 on 2022-06-16 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dentist', '0008_veneers'),
    ]

    operations = [
        migrations.AddField(
            model_name='veneers',
            name='titulli',
            field=models.CharField(default='Venners', max_length=255),
        ),
    ]
