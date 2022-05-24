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
  
 
 ### 결과 화면
|기능|UI|
|------|---|
|로그인기능(간략하게 구현)|<img src=images/login.png  width="60%" border="2"/>|
|고객(음식점 선택)|<img src=images/order_shops.png  width="70%" border="2"/>|
|고객(음식 주문)|<img src=images/order_menus.png  width="30%" border="2"/>|
|고객(주문 내역)|<img src=images/order_order.png  width="85%" border="2"/>|
|사장님(배달 예상 소요시간 입력)|<img src=images/boss_orders.png  width="85%" border="2"/>|
|배달기사님(배송완료후 배송완료 버튼 클릭)|<img src=images/delivery_orders.png  width="85%" border="2"/>|



  
  <br>

  <br>

***

