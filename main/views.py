from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from .models import Restaurant

def index(request):
    #restaurant_list = Restaurant.objects.order_by('-id')
    #output = ', '.join([q.resteraunt_name for q in restaurant_list])
    return HttpResponse('index')


def customer(request, customer_id):
    return HttpResponse('customer' + customer_id)


def reservation(request, reservation_id):
    return HttpResponse('reservation' + reservation_id)


def table(request, table_id):
    return HttpResponse('table' + table_id)


def restaurant(request, restaurant_id):
    return HttpResponse('restaurant' + restaurant_id)
