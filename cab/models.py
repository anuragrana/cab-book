from django.db import models

# Create your models here.
MOBILE_MAX_LENGTH = 10


class RiderModel(models.Model):
    user_id = models.AutoField(primary_key=True, null=False, blank=True)
    mobile = models.CharField(max_length=MOBILE_MAX_LENGTH, null=False, blank=False)
    email = models.CharField(max_length=128, null=False, blank=False)
    name = models.CharField(max_length=128, null=False, blank=False)
    address = models.CharField(max_length=512, null=True, blank=True)
    is_mobile_verified = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)
    created_date = models.DateTimeField(null=False, blank=True, auto_now_add=True)
    updated_date = models.DateTimeField(null=False, blank=True, auto_now=True)


class DriverModel(models.Model):
    user_id = models.AutoField(primary_key=True, null=False, blank=True)
    mobile = models.CharField(max_length=MOBILE_MAX_LENGTH, null=False, blank=False)
    vehicle_number = models.CharField(max_length=128, null=False, blank=False)
    name = models.CharField(max_length=128, null=False, blank=False)
    address = models.CharField(max_length=512, null=True, blank=True)
    is_mobile_verified = models.BooleanField(default=False)
    created_date = models.DateTimeField(null=False, blank=True, auto_now_add=True)
    updated_date = models.DateTimeField(null=False, blank=True, auto_now=True)


class LatestLocationModel(models.Model):
    sys_id = models.AutoField(primary_key=True, null=False, blank=True)
    user_id = models.IntegerField(unique=True, null=False, blank=True)  # driver id
    x_coordinate = models.FloatField(null=False, blank=False)
    y_coordinate = models.FloatField(null=False, blank=False)
    is_driver_available = models.BooleanField(default=True)
    created_date = models.DateTimeField(null=False, blank=True, auto_now_add=True)
    updated_date = models.DateTimeField(null=False, blank=True, auto_now=True)


class DriverAvailabilityModel(models.Model):
    sys_id = models.AutoField(primary_key=True, null=False, blank=True)
    user_id = models.IntegerField(unique=True, null=False, blank=True)  # driver id
    is_driver_available = models.BooleanField(default=True)
    updated_date = models.DateTimeField(null=False, blank=True, auto_now=True)


class TripHistoryModel(models.Model):
    sys_id = models.AutoField(primary_key=True, null=False, blank=True)
    driver_id = models.IntegerField(unique=True, null=False, blank=True)  # driver id
    rider_id = models.IntegerField(unique=True, null=False, blank=True)  # rider id
    start_x_coordinate = models.FloatField(null=False, blank=False)
    start_y_coordinate = models.FloatField(null=False, blank=False)
    end_x_coordinate = models.FloatField(null=False, blank=False)
    end_y_coordinate = models.FloatField(null=False, blank=False)
    created_date = models.DateTimeField(null=False, blank=True, auto_now_add=True)
