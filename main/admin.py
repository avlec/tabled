from django.contrib import admin

from .models import Customer, Reservation, Table, Restaurant

admin.site.register(Customer, Reservation, Table, Restaurant)