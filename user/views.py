from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from requests import request
from order.models import Shop, Menu, Order, Orderfood
from user.models import User
from order.serializers import ShopSerializer, MenuSerializer
from user.serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


@csrf_exempt
def user(request):
    if request.method == 'GET': # select
        user = User.objects.all()
        return render(request, 'user/user_list.html', {'user_list':user})
        
    elif request.method == 'POST': # 수정 by insomnia
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save() 
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def login(request):
    if request.method == 'POST':
        name = request.POST['name']
        try:
            if User.objects.get(user_name=name):
                request.session['user_id'] = User.objects.get(user_name=name).id
                return render(request, 'user/success.html')
        except:
            return render(request, 'user/fail.html')
    elif request.method == 'GET':
        return render(request, 'user/login.html')