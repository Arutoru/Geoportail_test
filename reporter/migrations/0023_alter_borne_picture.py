# Generated by Django 4.1 on 2022-12-08 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0022_auto_20200306_0041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borne',
            name='picture',
            field=models.ImageField(default='C:\\Users\\User\\Documents\\programmation\\python\\Django\\Geodjango\\agricom\\defaut.jpg', upload_to=''),
        ),
    ]