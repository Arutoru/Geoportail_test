# Generated by Django 2.2.5 on 2019-11-25 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0006_auto_20191125_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidence',
            name='picture',
            field=models.ImageField(upload_to=''),
        ),
    ]
