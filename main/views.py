from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db import models
from .models import Restaurant

def index(request):
    restaurant_list = Restaurant.objects.order_by('-id')
    template = loader.get_template('main/templates/intex.html')
    context = {
        'restaurant_list' : restaurant_list
    }
    return HttpResponse(template.render(context, request))


def customer(request, customer_id):
    return HttpResponse('customer' + customer_id)


def reservation(request, reservation_id):
    return HttpResponse('reservation' + reservation_id)


def table(request, table_id):
    return HttpResponse('table' + table_id)


def restaurant(request, restaurant_id):
    return HttpResponse('restaurant' + restaurant_id)
