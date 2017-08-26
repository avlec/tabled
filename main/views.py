from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db import models
from .models import *


def index(request):
    context = {
        'restaurant_list' : Restaurant.objects.all()
    }
    return render(request, 'index.html', context)


def customer(request, customer_id):
    Customer.objects.get(id=customer_id)
    return HttpResponse('customer' + customer_id)


def reservation(request, reservation_id):
    Reservation.objects.get(id=reservation_id)
    return HttpResponse('reservation' + reservation_id)


def table(request, table_id):
    Table.objects.get(id=table_id)
    return HttpResponse('table' + table_id)


def restaurant(request, restaurant_id):
    Restaurant.objects.get(id=restaurant_id)
    return HttpResponse('restaurant' + restaurant_id)
