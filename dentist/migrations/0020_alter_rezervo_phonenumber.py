# Generated by Django 4.0.5 on 2022-06-18 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dentist', '0019_rezervo_phonenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rezervo',
            name='phonenumber',
            field=models.IntegerField(),
        ),
    ]
