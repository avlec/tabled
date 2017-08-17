# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-17 03:31
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=128)),
                ('customer_email', models.EmailField(max_length=128)),
                ('customer_credit_number', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(9999999999999999), django.core.validators.MinValueValidator(0)])),
                ('customer_credit_security', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(999), django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('party_name', models.CharField(max_length=128)),
                ('party_size', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(30), django.core.validators.MinValueValidator(1)])),
                ('reservation_time', models.DateTimeField(verbose_name='date published')),
                ('reservation_client', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant_name', models.CharField(max_length=128)),
                ('restaurant_desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_min_seating', models.IntegerField(default=1)),
                ('table_max_seating', models.IntegerField(default=1)),
                ('reservations', models.ManyToManyField(to='main.Reservation')),
            ],
        ),
        migrations.AddField(
            model_name='restaurant',
            name='tables',
            field=models.ManyToManyField(to='main.Table'),
        ),
    ]