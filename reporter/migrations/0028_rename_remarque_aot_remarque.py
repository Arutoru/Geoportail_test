# Generated by Django 4.1.3 on 2023-02-20 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0027_aot_remarque_aot_statut'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aot',
            old_name='Remarque',
            new_name='remarque',
        ),
    ]
