from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from requests import request
from order.models import Shop, Menu, Order, Orderfood
from order.serializers import ShopSerializer, MenuSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


# 배송기사 1명이라고 가정.
@csrf_exempt
def order_list(request):
    if request.method == 'GET':
        order_list = Order.objects.all()
        return render(request, 'delivery/order_list.html', {'order_list':order_list})
    
    elif request.method == 'POST':
        order_item = Order.objects.get(pk=int(request.POST['order_id']))
        order_item.deliver_finish = 1
        order_item.save()
        return render(request, 'delivery/success.html')
        

        