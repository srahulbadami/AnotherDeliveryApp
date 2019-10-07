from django.db import models
from django.contrib.gis.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)


class Delivery_Agent(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	location = models.PointField(null=False, blank=False, srid=4326, verbose_name="Location")
	on_delivery = models.BooleanField(default=False)
	total_distance = models.IntegerField(default=0)
	REQUIRED_FIELDS = []


class Customer(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	location = models.PointField(null=False, blank=False, srid=4326, verbose_name="Location")


class Delivery(models.Model):
	customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)
	delivery_agent = models.ForeignKey(Delivery_Agent, on_delete=models.PROTECT)
	pickup_location = models.PointField(null=False, blank=False, srid=4326, verbose_name="Location")
	at_pickup = models.BooleanField(default=False)
	location = models.PointField(null=False, blank=False, srid=4326, verbose_name="Location")
	start_time = models.DateTimeField()
	end_time = models.DateTimeField(null=True, blank=True)
	completed = models.BooleanField(default=False)
	total_distance = models.IntegerField(default=0)
