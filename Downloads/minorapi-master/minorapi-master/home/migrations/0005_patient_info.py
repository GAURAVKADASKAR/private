# Generated by Django 5.0.1 on 2024-04-25 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_hospitalinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='patient_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hospital_name', models.CharField(max_length=300)),
                ('Bed_id', models.CharField(max_length=300, unique=True)),
                ('Ward_number', models.IntegerField()),
                ('Room_number', models.IntegerField()),
                ('Disease', models.CharField(max_length=200)),
                ('Bed_type', models.CharField(max_length=300)),
                ('patient_name', models.CharField(max_length=200)),
                ('patient_gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=300)),
                ('patient_age', models.PositiveBigIntegerField()),
                ('address', models.TextField()),
                ('mobile_number', models.PositiveBigIntegerField()),
                ('current_medication', models.TextField()),
                ('allergies', models.TextField()),
                ('past_surgeries', models.TextField()),
                ('insurance_policy', models.TextField()),
                ('Policy_number', models.TextField()),
                ('special_request', models.TextField()),
            ],
        ),
    ]
