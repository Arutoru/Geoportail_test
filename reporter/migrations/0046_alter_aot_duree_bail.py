# Generated by Django 4.1.3 on 2024-03-19 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0045_alter_aot_bp_alter_aot_date_caution_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aot',
            name='duree_bail',
            field=models.IntegerField(default=None, verbose_name='Durée Bail (ans)'),
        ),
    ]
