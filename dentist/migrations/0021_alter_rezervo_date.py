# Generated by Django 4.0.5 on 2022-06-18 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dentist', '0020_alter_rezervo_phonenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rezervo',
            name='date',
            field=models.DateField(default='2022-1-1', verbose_name='Purchase Date(year/mm/day)'),
        ),
    ]
