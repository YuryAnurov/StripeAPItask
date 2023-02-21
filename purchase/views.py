import os
from dotenv import load_dotenv
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from .models import Item, Order
import stripe


load_dotenv()
stripe.api_key = os.getenv('STRIPE_SECRET_KEY')


def index(request, stat=None):
# Обнуляем принадлежность товаров к заказу
    for item in Item.objects.all():
        item.counter = 0
        item.order = None
        item.save()
# Удаляем все заказы кроме текущего
    for order in Order.objects.all():
        order.delete()
    order = Order()
    order.save()
    load_dotenv()
    stripepk = os.getenv('STRIPE_PUBLISHABLE_KEY')
    return render(request, "purchase/index.html", {"items":Item.objects.all(), "order":order, 'stripepk':stripepk, 'status':stat})


def buy_item(request, orderitem, item_id):
    if orderitem == 'order':
        item = Order.objects.get(id=item_id)
    elif orderitem == 'item':
        item = Item.objects.get(id=item_id)
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
       'price_data': {
                'currency': 'rub',
                'product_data': {
                    'name': item.name,
                    'description': item.description,
                    },
                'unit_amount': int(item.price * 100),
            },
        'quantity': 1,     
        }],
    mode='payment',
    success_url='http://127.0.0.1:8000/status/success',
    cancel_url='http://127.0.0.1:8000/status/cancel',
      )
    return JsonResponse({'session_id': session.id})


def get_item(request, orderitem, item_id):
    try:
        if orderitem == 'order':
            item = Order.objects.get(id=item_id)
        elif orderitem == 'item':
            item = Item.objects.get(id=item_id)
        itemdata = {
            'id': item.id,
            'name': item.name,
            'description': item.description,
            'price': item.price,
        }
        return JsonResponse(itemdata)
    except ObjectDoesNotExist:
        return JsonResponse({'error': f'Item with id {id} not found.'}, status=404)
    

def itemqnt(request, order_id, item_id, counter):
    try:
        item = Item.objects.get(id=item_id)
        order = Order.objects.get(pk=order_id)
        item.order = order
        item.counter = counter
        item.save()
        order.price = order.fprice()
        order.description = order.fdescription()
        order.save()
        orderdata = {
            'description': order.fdescription(),
            'price': order.fprice(),
        }
        return JsonResponse(orderdata)
    except ObjectDoesNotExist:
        return JsonResponse({'error': f'Item with id {id} not found.'}, status=404)
