from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db import models
from .models import *

def home(request):
    return render(request, 'home.html')

def index(request):
    context = {
        'restaurant_list': Restaurant.objects.all(),
        'title': 'Get a Table',
        'current_page': 'customer.html',
    }
    return render(request, 'index.html', context)


def customer(request, customer_id):
    Customer.objects.get(id=customer_id)
    context = {
        'title': 'Get a Table',
        'current_page': 'customer.html',
    }
    return render(request, 'customer.html', context)

def reservation(request, reservation_id):
    Reservation.objects.get(id=reservation_id)
    context = {
        'title': 'Get a Table',
        'current_page': 'customer.html',
    }
    return render(request, 'reservation.html', context)


def table(request, table_id):
    Table.objects.get(id=table_id)
    context = {
        'title': 'Get a Table',
        'current_page': 'customer.html',
    }
    return render(request, 'table.html', context)


def restaurant(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    context = {
        'title' : restaurant.restaurant_name,
        'current_page': 'customer.html',
    }
    return render(request, 'restaurant.html', context)
