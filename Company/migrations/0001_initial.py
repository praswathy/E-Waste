# Generated by Django 5.0.3 on 2024-04-04 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_waste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('waste_category', models.CharField(max_length=50)),
                ('waste_quantity', models.IntegerField()),
            ],
        ),
    ]
