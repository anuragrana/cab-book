# Generated by Django 2.2.9 on 2020-04-02 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DriverModel',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('mobile', models.CharField(max_length=10)),
                ('vehicle_number', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=128)),
                ('address', models.CharField(blank=True, max_length=512, null=True)),
                ('is_mobile_verified', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='LatestLocationModel',
            fields=[
                ('sys_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField(blank=True, unique=True)),
                ('x_coordinate', models.FloatField()),
                ('y_coordinate', models.FloatField()),
                ('is_driver_available', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='RiderModel',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('mobile', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=128)),
                ('address', models.CharField(blank=True, max_length=512, null=True)),
                ('is_mobile_verified', models.BooleanField(default=False)),
                ('is_email_verified', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TripHistoryModel',
            fields=[
                ('sys_id', models.AutoField(primary_key=True, serialize=False)),
                ('driver_id', models.IntegerField(blank=True, unique=True)),
                ('start_x_coordinate', models.FloatField()),
                ('start_y_coordinate', models.FloatField()),
                ('end_x_coordinate', models.FloatField()),
                ('end_y_coordinate', models.FloatField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
