# Generated by Django 4.0.5 on 2022-06-16 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dentist', '0007_galeria_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Veneers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descriptioN', models.TextField()),
                ('foto', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
