from django.urls import path
from . import views

urlpatterns = [
path('<obj>',views.materials,name='materials'),

]