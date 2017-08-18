from django.contrib import admin

from .models import Customer, Reservation, Table, Restaurant

admin.site.register(Customer)
admin.site.register(Reservation)
admin.site.register(Table)
admin.site.register(Restaurant)