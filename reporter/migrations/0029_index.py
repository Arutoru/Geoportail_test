# Generated by Django 4.1.3 on 2023-02-27 11:18

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0028_rename_remarque_aot_remarque'),
    ]

    operations = [
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objectid', models.IntegerField()),
                ('join_count', models.IntegerField()),
                ('target_fid', models.IntegerField()),
                ('join_fid', models.IntegerField()),
                ('id_index', models.IntegerField()),
                ('code_tarif', models.IntegerField()),
                ('compteur', models.IntegerField()),
                ('nouvel_ind', models.IntegerField()),
                ('ancien_ind', models.IntegerField()),
                ('coef', models.IntegerField()),
                ('conso_m3', models.BigIntegerField()),
                ('prix_unit', models.BigIntegerField()),
                ('mont_conso', models.BigIntegerField()),
                ('entretien', models.BigIntegerField()),
                ('mont_payer', models.BigIntegerField()),
                ('amodiatair', models.CharField(max_length=50)),
                ('rccm', models.CharField(max_length=50)),
                ('niu', models.CharField(max_length=50)),
                ('bp', models.CharField(max_length=50)),
                ('tel', models.BigIntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPointField(srid=32632)),
            ],
        ),
    ]
