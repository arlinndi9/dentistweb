# Generated by Django 4.0.5 on 2022-06-29 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dentist', '0023_alter_pricing_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='rezervo',
            name='color',
            field=models.CharField(choices=[('green', 'GREEN'), ('blue', 'BLUE'), ('red', 'RED'), ('orange', 'ORANGE'), ('black', 'BLACK')], default='red', max_length=10),
        ),
    ]