# Generated by Django 5.0.3 on 2024-03-12 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adminstrator', '0009_tbl_adminregistration_tbl_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_Name', models.CharField(max_length=50)),
            ],
        ),
    ]
