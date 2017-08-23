from django.conf.urls import url

from . import views

# TODO sub categorize each
# <restaurant_id>/reservation/<reservation_id>/
# <restaurant_id>/table/<table_id>


urlpatterns = [
    # ex /main
    url(r'^$', views.index, name='index'),

    # TODO use name instead of id
    # ex /main/restaurant/12/
    url(r'^restaurant/(?P<restaurant_id>[0-9]+)/$', views.restaurant, name='table'),

    # ex /main/12/
    url(r'^customer/(?P<customer_id>[0-9]+)/$', views.customer, name='customer'),

    # ex /main/customer/12/
    url(r'^reservation/(?P<reservation_id>[0-9]+)/$', views.reservation, name='reservation'),

    # ex /main/reservation/12/
    url(r'^table/(?P<table_id>[0-9]+)/$', views.table, name='table'),

]
