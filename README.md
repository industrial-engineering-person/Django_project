# Django_project
> 온라인 주문 어플리케이션 백엔드 만들기
 <br>

## Description

> 2022.05.진행
### Bounded Context

<img src=images/Bounded_context.png  width="60%"/>


  
  <br>

### Summary

* User_order(고객-Django)에서 고객주문과 Boss(가게 사장님-Flask)의 백엔드 MYSQL을 각각 독립적으로 분리
* Internal API를 통해 각 DB의 초기값 세팅 및 테스트 by insomnia
* RabbitMQ를 사용한 상호 DB data의 consistency 유지

  

  

  <br>

  <br>
  
 
 ### result

* User_order(Django) MYSQL에서 가게(Shop) 또는 주문(Order)가 생성되거나 수정되나 삭제될 시 Boss(Flask)에 RabbitMQ가 producing함
* Boss(Flask)에서 consuming을 받고 routing_key(order_created, order_updated, order_deleted 등)에 따라 MYSQL이 consistance를 유지함

  
  <br>

  <br>

***

