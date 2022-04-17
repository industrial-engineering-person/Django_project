from django.contrib import admin
from .models import Shop, Menu, Order, Orderfood

# 개발자가 아닌 관리자를 위한 admin UI 관리
admin.site.register(Shop)
admin.site.register(Menu)
admin.site.register(Order)
admin.site.register(Orderfood)