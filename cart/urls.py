from django.urls import path
from . import views

urlpatterns = [
path('info/media/pics/<obj>/<obj1>/<obj2>/<obj3>/<obj4>/<obj5>',views.info,name='info'),
path('saving',views.saving,name='saving'),
path('viewing',views.viewing,name='viewing'),

path('deleting/<int:obj>',views.deleting,name='deleting'),
path('detailsinfo/media/pics/<obj1>/<obj2>/<obj3>/<obj4>/<obj5>/<obj6>/<obj7>',views.detailsinfo,name='detailsinfo'),
path('order_saving',views.order_saving,name="order_saving"),
path('order_viewing',views.order_viewing,name="order_viewing"),
path('order_deleting/<int:obj1>',views.order_deleting,name='order_deleting'),
]