from django.db import models

# DB(MYSQL)의 각 table setting

# 주문자가 상점에 메뉴들을 보고 선택해야하기 위한 상점 / pk는 자동생성
class Shop(models.Model):
    shop_name = models.CharField(max_length=20)
    shop_address = models.CharField(max_length=40)
    def __str__(self):
        return self.shop_name
    
# 상점 내의 메뉴들
class Menu(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=20) # food table 따로 빼지않고 진행
    def __str__(self):
        return self.food_name
    
# 특정 주문자가 주문한 내역들
class Order(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    order_date = models.DateTimeField('date ordered')
    address = models.CharField(max_length=40)
    
    estimated_time = models.IntegerField(default=-1) # 배송 예상시간
    deliver_finish = models.IntegerField(default=0) # 배송 완료시간
    
# 한 Order안에 있는 메뉴 리스트
class Orderfood(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE) # 최대한 중복없이
    food_name = models.CharField(max_length=20)
    