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
|로그인기능(간략하게 구현)|<img src=images/login.png  width="55%" border="2"/>|
|고객(음식점 선택)|<img src=images/order_shops.png  width="75%" border="2"/>|
|고객(음식 주문)|<img src=images/order_menus.png  width="30%" border="2"/>|
|고객(주문 내역)|<img src=images/order_order.png  width="90%" border="2"/>|
|사장님(배달 예상 소요시간 입력)|<img src=images/boss_orders.png  width="90%" border="2"/>|
|배달기사님(배송완료후 배송완료 버튼 클릭)|<img src=images/delivery_orders.png  width="90%" border="2"/>|



  
  <br>

  <br>
## Repository 구조

```
.
├── boss                    # 사장님 
├── delivery                # 배달 기사 앱 파일
├── django_project          # config 파일
├── images                  # README.md 용 이미지
├── order                   # 고객 주문 파일
├── static                  # 부트스트랩 템플릿 파일
├── user                    # 로그인 파일
├── README.md
├── db.sqlite3              # 간이 배포용 sqlite3 / 타 DB로 확장가능
├── manage.py
└── requirements.txt        # 프레임워크, 라이브러리 버전
 
```
 <br>
 
 <br> 
 
 
## Repository 구조의 예를 들면 다음과 같습니다.

```
.
├── airflow_py              # MWAA 활용 전 local 환경에서 airflow를 정리한 파일
├── notebook                # aws emr에서 batch processing code
├── script                  # MWAA에서 필요로하는 dag파일과 emr steps용 파일
└── README.md    # MWAA에서 필요로하는 dag파일과 emr steps용 파일
 
```


<br>
***

