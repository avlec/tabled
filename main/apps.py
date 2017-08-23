from django.apps import AppConfig


class MainConfig(AppConfig):
    name = 'tabled'
    label = 'tabled'
    verbose_name = 'Tabled'

    def ready(self):
        from .models import Customer, Reservation, Table, Restaurant
