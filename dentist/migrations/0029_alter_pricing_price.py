# Generated by Django 4.0.5 on 2022-09-04 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dentist', '0028_mendimi_lastname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricing',
            name='price',
            field=models.IntegerField(verbose_name='Price'),
        ),
    ]