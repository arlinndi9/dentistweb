# Generated by Django 4.0.5 on 2022-06-29 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dentist', '0025_alter_rezervo_color'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rezervo',
            old_name='color',
            new_name='sherbimi',
        ),
    ]