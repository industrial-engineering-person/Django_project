# Django_project
> 온라인 주문 어플리케이션 Django 백엔드 만들기
 <br>
* 프론트엔드는 일부 가시성을 위해 부트스트랩을 적용하였지만 백엔드 설계에 초점을 맞췄습니다.

## Description

> 2022.05.진행
### Bounded Context

<img src=images/Bounded_context.png  width="60%"/>


  
  <br>

### Summary

* 로그인 시 손님 / 가게사장님 / 배달기사님 총 3분류로 로그인이 되어 각 UI가 다르게 적용된다. (Django Session 활용)
* 고객은 음식점을선택후 음식과 주소를 작성하여 주문을 한다.
* 사장님은 고객에게 배송 예상소요시간을 입력한다.
* 배달기사님은 배송완료 시 배송완료 버튼을 클릭한다.

  

  

  <br>

  <br>
  
 
 ### result 

* User_order(Django) MYSQL에서 가게(Shop) 또는 주문(Order)가 생성되거나 수정되나 삭제될 시 Boss(Flask)에 RabbitMQ가 producing함
* Boss(Flask)에서 consuming을 받고 routing_key(order_created, order_updated, order_deleted 등)에 따라 MYSQL이 consistance를 유지함

  
  <br>

  <br>

***

