from django.shortcuts import render
from .models import Products, Orders, OrderUpdate
from math import ceil
# Create your views here.

def index(request):
    """products = Products.objects.all()
    n = len(products)
    nSlides = n//4 + ceil((n/4) + (n//4))
    allProds = [[products, range(1, nSlides), nSlides], [products, range(1, nSlides), nSlides]]
    context = {'allProds' : allProds}"""

    allProds = []
    catprods = Products.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Products.objects.filter(category=cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4) + (n//4))
        allProds.append([prod, nSlides, range(1, nSlides)])


    context = {'allProds': allProds}
    return render(request, 'homepage.html', context)


def viewProduct(request, id):
    product = Products.objects.filter(id = id)
    context = {'product':product}
    return render(request, 'productview.html', context)


def checkout(request):
    if request.method == 'POST':
        items = request.POST.get('items')
        name = request.POST.get('name')
        address = request.POST.get('address1') +" "+ request.POST.get('address2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zipcode = request.POST.get('zipcode')
        mobile_no = request.POST.get('mobile_no')

        order = Orders(items=items, name= name, address = address, city= city, state=state, zipcode=zipcode, mobile_no=mobile_no)
        order.save()
        update = OrderUpdate(order_id=order.order_id, desc="Order has been placed", mobile_no=mobile_no)
        update.save()
        thank = True
        id = order.order_id
        context = {'thank':thank, 'id':id}
        return render(request, 'checkout.html', context)

    return render(request, 'checkout.html')

def tracker(request):
    if request.method == 'POST':
        order_id = request.POST.get('orderId')
        mobile = request.POST.get('mobile')
        if(mobile == '' or order_id == ''):
            return render(request, 'tracker.html')
        try:
            checkOrder = OrderUpdate.objects.filter(order_id=order_id,mobile_no=mobile)
            print(checkOrder)
            params = {'orderupdate':checkOrder}
            return render(request, 'tracker.html', params)
        except Exception as e:
            mssg = "Error : Please check your details submitted and try again !! Incorrect details"
            params = {'message', mssg}
            return render(request, 'tracker.html', params)
    return render(request, 'tracker.html')