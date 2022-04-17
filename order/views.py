from time import time
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from requests import request
from order.models import Shop, Menu, Order, Orderfood
from order.serializers import ShopSerializer, MenuSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

# ref : https://www.django-rest-framework.org/tutorial/1-serialization/

@csrf_exempt
def shop(request):
    if request.method == 'GET': # select
        # shop = Shop.objects.all() # insomnia test용
        # serializer = ShopSerializer(shop, many=True) # DB 데이터는 Json이 아니기에 Json으로 바꾸는 Serialize
        # return JsonResponse(serializer.data, safe=False)
        shop = Shop.objects.all()
        return render(request, 'order/shop_list.html', {'shop_list':shop})
        
    elif request.method == 'POST': # 수정
        data = JSONParser().parse(request)
        serializer = ShopSerializer(data=data)
        if serializer.is_valid():
            serializer.save() # 형식이 맞아서 정상적으로 DB update
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

# request.POST['address']

@csrf_exempt
def menu(request, shop):
    if request.method == 'GET': # select 
        menu = Menu.objects.filter(shop=shop) # Menu.objects.get은 1개의 obj만 받음
        return render(request, 'order/menu_list.html', {'menu_list':menu, 'shop':shop})
        
    elif request.method == 'POST': # 수정
        data = JSONParser().parse(request)
        serializer = MenuSerializer(data=data)
        if serializer.is_valid():
            serializer.save() # 형식이 맞아서 정상적으로 DB update
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
from django.utils import timezone
 
@csrf_exempt
def order(request):
    if request.method == 'POST':
        address = request.POST['address']
        order_date = timezone.now()
        shop = request.POST['shop']
        food_list = request.POST.getlist('menu')
        
        shop_item = Shop.objects.get(pk=int(shop))
        shop_item.order_set.create(address=address, order_date=order_date, shop=int(shop)) # 저장
        
        order_item = Order.objects.get(pk=shop_item.order_set.latest('id').id)
        order_item.orderfood_set.create(food_name=food_list)
        
        return render(request, 'order/success.html')
    elif request.method == 'GET':
        order_list = Order.objects.all()
        return render(request, 'order/order_list.html', {'order_list':order_list})