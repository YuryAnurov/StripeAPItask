from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path("status/<str:stat>", views.index, name="status"),
    path('getitem/<str:orderitem>/<int:item_id>/',views.get_item,name='get_item'),
    path('buyitem/<str:orderitem>/<int:item_id>/',views.buy_item,name='buy_item'),
    path('itemqnt/<int:order_id>/<int:item_id>/<int:counter>/',views.itemqnt,name='item_qnt'),
]