from django.apps import AppConfig


class MainConfig(AppConfig):
    name = 'tabled'
    label = 'tabled'
    verbose_name = 'Tabled'

    def ready(self):
        Customer = self.get_model('Customer')
        Reservation = self.get_model('Reservation')
        Table = self.get_model('Table')
        Restaurant = self.get_model('Restaurant')