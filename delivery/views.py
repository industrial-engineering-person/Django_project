from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from requests import request
from order.models import Shop, Menu, Order, Orderfood
from user.models import User
from order.serializers import ShopSerializer, MenuSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


# 배송기사 1명이라고 가정.
@csrf_exempt
def order_list(request):
    if request.method == 'GET':
        # order_list = Order.objects.all()
        # return render(request, 'delivery/order_list.html', {'order_list':order_list})
        try:
            if User.objects.get(id=request.session['user_id']).user_type == 2:
                order_list = Order.objects.all()
                return render(request, 'delivery/order_list.html', {'order_list':order_list})
            else:
                return render(request, 'delivery/fail.html')
        except:
            return render(request, 'delivery/fail.html')
    
    elif request.method == 'POST':
        order_item = Order.objects.get(pk=int(request.POST['order_id']))
        order_item.deliver_finish = 1
        order_item.save()
        return render(request, 'delivery/success.html')
        

        