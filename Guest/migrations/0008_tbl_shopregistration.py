# Generated by Django 5.0.3 on 2024-03-19 06:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adminstrator', '0023_delete_tbl_shopregistration'),
        ('Guest', '0007_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_shopregistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopregistration_name', models.CharField(max_length=50)),
                ('shopregistration_contact', models.CharField(max_length=50)),
                ('shopregistration_email', models.CharField(max_length=50)),
                ('shopregistration_password', models.CharField(max_length=50)),
                ('shopregistration_address', models.CharField(max_length=50)),
                ('shopregistration_photo', models.FileField(upload_to='Assets/shopregistrationPhoto/')),
                ('shopregistration_proof', models.FileField(upload_to='Assets/shopregistrationProof/')),
                ('shopregistration_status', models.IntegerField(default='0')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Adminstrator.tbl_place')),
            ],
        ),
    ]
