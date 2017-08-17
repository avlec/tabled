import datetime

from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

__all__ = ['Customer', 'Reservation', 'Table', 'Restaurant']

class Customer(models.Model):
    customer_name = models.CharField(max_length=128)
    customer_email = models.EmailField(max_length=128)
    customer_credit_number = models.IntegerField(default=0,validators=[MaxValueValidator(9999999999999999), MinValueValidator(0)])
    customer_credit_security = models.IntegerField(default=0,validators=[MaxValueValidator(999), MinValueValidator(0)])



class Reservation(models.Model):
    party_name = models.CharField(max_length=128)
    party_size = models.IntegerField(default=1, validators=[MaxValueValidator(30), MinValueValidator(1)])
    reservation_time = models.DateTimeField('date published')
    reservation_client = models.OneToOneField(Customer)
    def __str__(self):
        return self.party_name + ' for ' + self.party_size + ' at [' + self.reservation_time + ']'


class Table(models.Model):
    reservations = models.ManyToManyField(Reservation)
    table_min_seating = models.IntegerField(default=1)
    table_max_seating = models.IntegerField(default=1)


class Restaurant(models.Model):
    tables = models.ManyToManyField(Table)
    restaurant_name = models.CharField(max_length=128)
    restaurant_desc = models.TextField()
