# Generated by Django 5.0.1 on 2024-02-14 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_rename_hospital_hospitalname'),
    ]

    operations = [
        migrations.DeleteModel(
            name='hospitalname',
        ),
    ]
