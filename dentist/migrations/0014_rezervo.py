# Generated by Django 4.0.5 on 2022-06-18 17:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dentist', '0013_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rezervo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('addresa', models.CharField(max_length=255)),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Purchase Date(mm/dd/year)')),
                ('message', models.TextField()),
            ],
        ),
    ]