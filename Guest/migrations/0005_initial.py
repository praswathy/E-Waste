# Generated by Django 5.0.3 on 2024-03-14 07:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Adminstrator', '0016_tbl_employee'),
        ('Guest', '0004_delete_tbl_newuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_newuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Newuser_name', models.CharField(max_length=50)),
                ('Newuser_gender', models.CharField(max_length=50)),
                ('Newuser_contact', models.CharField(max_length=50)),
                ('Newuser_email', models.CharField(max_length=50)),
                ('Newuser_password', models.CharField(max_length=50)),
                ('Newuser_confirmpassword', models.CharField(max_length=50)),
                ('Newuser_dob', models.CharField(max_length=50)),
                ('Newuser_address', models.CharField(max_length=50)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Adminstrator.tbl_district')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Adminstrator.tbl_place')),
            ],
        ),
    ]
