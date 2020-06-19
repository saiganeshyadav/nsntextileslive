from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import HttpResponse
from .models import Cartitems,Order


from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string



# Create your views here.

def info(request,obj,obj1,obj2,obj3,obj4,obj5):
    img=obj
    name=obj1
    cost=int(obj2)
    pcs=int(obj3)
    size=obj4
    cust=obj5

    li=[]
    lp=[]

    ref="pics/"+img

    cartitems=Cartitems.objects.all()

    for memb in cartitems:
        if memb.customer == cust:
            li = li + [memb.item_name]
            lp = lp + [memb.item_image]

    print(ref)
    return render(request,'info_form.html',{'img':img,'name':name,'cost':cost,'pcs':pcs,'size':size,'li':li,'lp':lp,'ref':ref})

def saving(request):
    customer = request.POST["customer"]
    item_name = request.POST["item_name"]
    item_price = request.POST["item_price"]
    item_image = request.POST["item_image"]
    item_pcs = request.POST["item_pcs"]
    item_size = request.POST["item_size"]


    cartitems= Cartitems(customer=customer,item_name=item_name,item_image=item_image,item_price=item_price,item_pcs=item_pcs,item_size=item_size)
    cartitems.save()

    return redirect("/cart/viewing")

def viewing(request):

    cartitems=Cartitems.objects.all()

    listof = []


    if request.user.is_authenticated:
        for mem in cartitems:
            if mem.customer == request.user.username:
                listof = listof + [mem.item_name]

    le = len(listof)






    return render(request,'cart.html',{'cartitems':cartitems,'le':le})



def deleting(request,obj):
    thing=Cartitems.objects.get(id=obj)
    thing.delete()
    return redirect('/cart/viewing')



def detailsinfo(request,obj1,obj2,obj3,obj4,obj5,obj6,obj7):
    ord_img = obj1
    ord_name = obj2
    ord_size = obj3
    ord_pcs = int(obj4)
    ord_price = int(obj5)
    ord_id = int(obj7)


    return render(request,'details_info.html',{'ord_img':ord_img,'ord_name':ord_name,'ord_size':ord_size,'ord_pcs':ord_pcs,'ord_price':ord_price,'ord_id':ord_id})


def order_saving(request):
    shop_name = request.POST["shop_name"]
    adress = request.POST["adress"]
    shop_email = request.POST["shop_email"]
    shop_number = request.POST["shop_number"]

    cust_name = request.POST['person']
    ord_name = request.POST['ord_name']
    ord_img = request.POST['ord_img']
    ord_size = request.POST['ord_size']
    ord_pcs = request.POST['ord_pcs']
    ord_price = request.POST['ord_price']
    ord_id = request.POST['ord_id']
    order = Order(shop_name=shop_name,adress=adress,shop_email=shop_email,shop_number=shop_number,cust_name=cust_name,ord_name=ord_name,ord_img=ord_img,ord_size=ord_size,ord_pcs=ord_pcs,ord_price=ord_price)

    order.save()

    waste = Cartitems.objects.get(id=ord_id)
    waste.delete()

    templete1 = render_to_string('order_sending.html', {'shop_name': shop_name,'ord_name':ord_name})

    gmail1 = EmailMessage(
        'Thanks! For Shopping..',
        templete1,
        settings.EMAIL_HOST_USER,
        [shop_email],

    )

    gmail1.fail_silently = False
    gmail1.send()

    return redirect('/cart/order_viewing')


def order_viewing(request):

    order = Order.objects.all()

    listoford = []

    if request.user.is_authenticated:
        for memu in order:
            if memu.cust_name == request.user.username:
                listoford = listoford + [memu.ord_name]

    lenn = len(listoford)



    return render(request,'order_viewing.html',{'order':order,'lenn':lenn})



def order_deleting(request,obj1):

    wanttodel = Order.objects.get(id=obj1)
    wanttodel.delete()

    return redirect('/cart/order_viewing')

