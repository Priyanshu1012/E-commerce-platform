from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from shopkeeper.models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
def index(request):
    cart = request.session.get('cart')
    print(cart)
    if not cart:
        request.session['cart'] = {}
    template = "index.html"
    item_data = Items.objects.all()[:12]
    context= {'item_data':item_data}
    return render(request,template,context)

def search_item(request):
    template = "index.html"
    if request.method == 'POST':
        search_result = request.POST['search']
        results = []
        if(search_result!=""):
            templatename = "index.html"
            lookups = Q(name__icontains = search_result)
            results = Items.objects.filter(lookups)
            if(len(results) == 0):
                return HttpResponse('no value found')
            else:
                context = {'item_data': results}
                return render(request, template, context)
        else:
            return(index(request))


def Women(request):
    template = "women.html"
    kapda=[]
    item_data = Items.objects.filter(type="Women")
    for i in item_data:
        kapda.append(i.name)
    kapda=list(set(kapda))
    print(kapda)
    context = {'item_data':item_data,
               'women_data':kapda}
    return render(request,template,context)



def Men(request):
    template = "men.html"
    kapda = []
    item_data = Items.objects.filter(type="Men")
    for i in item_data:
        kapda.append(i.name)
    kapda = list(set(kapda))
    print(kapda)
    context = {'item_data': item_data,
               'men_data': kapda}
    return render(request, template, context)

def category(request,type,name):
    template = 'Category.html'
    valid = Items.objects.all().filter(name=name,type=type)
    filter_data = set(Items.objects.values_list('name',flat=True).filter(type=type))
    data = Items.objects.values_list('type',flat=True).filter(name=name,type=type)
    cat_type = data[0]
    context = {'cat_data':valid,'cat_type':cat_type,'filter_data':filter_data}
    return render(request, template, context)

def allProductCategory(request,name):
    template = 'Category.html'
    valid = Items.objects.all().filter(name=name)
    filter_data = set(Items.objects.values_list('name',flat=True).filter(type=type))
    data = Items.objects.values_list('type',flat=True).filter(name=name,type=type)
    cat_type = data[0]
    context = {'cat_data':valid,'cat_type':cat_type,'filter_data':filter_data}
    return render(request, template, context)

def Products(request):
    template = "products.html"
    kapda = []
    item_data = Items.objects.all()
    for i in item_data:
        kapda.append(i.name)
    kapda=list(set(kapda))
    context = {'item_data':item_data,
               'kapda_data':kapda}
    return render(request,template,context)

def Account(request):
    template = "account.html"
    context = {}
    return render(request,template,context)

def Register_page(request):
    template = "register.html"
    context = {}
    return render(request,template,context)

def registerSubmit(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email_address = request.POST['email_address']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
    data = Register(
        first_name = first_name,
        last_name = last_name,
        email_address = email_address,
        password = password,
        confirm_password = confirm_password
    )
    data.save()

    template="account.html"
    context={}
    return render(request,template,context)

def loginSubmit(request):
    if request.method == 'POST':
        email_address = request.POST['email_address']
        password = request.POST['password']
        try:
            valid = Register.objects.all().filter(email_address=email_address,password=password)
        except Exception as e:
            print(e)
        for i in valid:
            get_email = i.email_address
            get_pass = i.password
        if(valid):
            request.session['email_address'] = get_email
            request.session['password'] = get_pass
            return index(request)
        else:
            return HttpResponse('FIRST YOU HAVE TO REGISTER')
    print(request.user)


def Contact_page(request):
    template = "contact.html"
    context = {}
    return render(request, template, context)

def Contactsubmit(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phonenumber = request.POST['phonenumber']
        message = request.POST['message']
    data = Contact(
        name = name,
        email = email,
        phonenumber = phonenumber,
        message = message
    )
    data.save()

    template = "contact.html"
    context = {}
    return render(request,template,context)

def Single_product(request,id):
    template = "single.html"
    item_data = Items.objects.values('name','image','price').filter(id=id)
    context = {'item_data': item_data}
    return render(request,template,context)


def add_to_cart(request,id):
    product = id
    cart = request.session.get('cart')
    if cart:
        quantity = cart.get(product)

        if quantity:
            cart[product] = quantity + 1
        else:
            cart[product] = 1
    else:
        cart = {}
        cart[product] = 1
    
    request.session['cart'] = cart
    data = Items.objects.filter(id=id)
    for i in data:
        name = i.name
        price = i.price
        image_cart = i.image
        total_price = cart[product]*i.price
    print(cart[product])
    data = Cart(
        id = id,
        name = name,
        quantity = cart[product],
        price = price,
        total_price = total_price,
        image_cart = image_cart
    )
    data.save()

    template = "index.html"
    item_data = Items.objects.all()[:12]
    context= {'item_data':cart[product]}
    return JsonResponse(context)


def delete_from_cart(request,id):
    product = id
    cart = request.session.get('cart')
    quantity = cart.get(product)
    print(quantity)
    if quantity<=1:
        print(cart)
        cart.pop(product)
        print(cart)
        item_quantity=0
        
        
    else:
        item_quantity = quantity-1 
        cart[product] = quantity-1  
        
    request.session['cart'] = cart

    data = Items.objects.filter(id=id)
    for i in data:
        name = i.name
        image_cart = i.image
        price = i.price
    if(item_quantity==0):
        Cart.objects.filter(id=id).delete()
    else:
        d = Cart.objects.filter(id=id)
        for i in d:
            total_price = i.total_price
        data = Cart(
            id = id,
            name = name,
            quantity = cart[product],
            price = price,
            total_price = total_price,
            image_cart = image_cart
        )
        data.save()

    template = "index.html"
    item_data = Items.objects.all()[:12]
    context= {'item_data': item_quantity}
    return JsonResponse(context)
        
def logout (request):
    request.session.clear()
    Cart.objects.all().delete()
    template = "account.html"
    context= {}
    return render(request,template,context)

def showcart(request):

    template = "Cart.html"
    cart_data = Cart.objects.all()[:]
    if cart_data.exists():
        total_product_price = 0
        for i in cart_data:
            c = i.total_price
            total_product_price = total_product_price + c
        context= {'cart_data':cart_data,'total_product_price':total_product_price}
        return render(request,template,context)
    else:
        template = "Cart.html"
        context= {'cart_data':cart_data,'error':1}
        return render(request,template,context)

def delete_product(request,id):
    Cart.objects.filter(id=id).delete()
    del request.session['cart'][id]
    request.session.modified = True
    return (showcart(request))

