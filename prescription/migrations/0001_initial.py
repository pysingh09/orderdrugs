# Generated by Django 3.1.7 on 2021-03-09 10:29

import django.db.models.deletion
import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('address_1', models.CharField(max_length=128)),
                ('address_2', models.CharField(blank=True, max_length=128, null=True)),
                ('city', models.CharField(max_length=64)),
                ('state', models.CharField(max_length=128)),
                ('zip_code', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=30)),
                ('age', models.PositiveIntegerField(default=0)),
                ('sex',
                 models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=40)),
                ('type',
                 models.CharField(choices=[('doctor', 'Doctor'), ('chemist', 'Chemist'), ('patient', 'Patient')],
                                  max_length=40)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Drugs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('price', models.PositiveIntegerField(default=0)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('benefit', models.TextField(blank=True, null=True)),
                ('side_effect', models.TextField(blank=True, null=True)),
                ('advice', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Medicines',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('drugs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prescription.drugs')),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('symptoms', models.TextField()),
                ('precautions', models.TextField(blank=True, null=True)),
                ('medicines',
                 models.ManyToManyField(related_name='prescribed_medicine', through='prescription.Medicines',
                                        to='prescription.Drugs')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient',
                                              to=settings.AUTH_USER_MODEL)),
                ('prescriber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor',
                                                 to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pharmacy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('address_1', models.CharField(max_length=128)),
                ('address_2', models.CharField(blank=True, max_length=128, null=True)),
                ('city', models.CharField(max_length=64)),
                ('state', models.CharField(max_length=128)),
                ('zip_code', models.CharField(max_length=10)),
                ('website', models.URLField()),
                ('name', models.CharField(max_length=50)),
                ('drugs', models.ManyToManyField(to='prescription.Drugs')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='medicines',
            name='prescription',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medicines_prescription',
                                    to='prescription.prescription'),
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('amount', models.PositiveIntegerField(default=0)),
                (
                'pharmacy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prescription.pharmacy')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_prescription',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_prescription',
                                   to='prescription.prescription')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
