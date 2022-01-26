from users.decorators import allowed_user, staff_only
from django.contrib.auth.models import User
from products.forms import BrandsForm, CategoryForm, ProductForm, cleanForm, constForm, orderForm, plumbForm, serviceForm
from django.core import paginator
from products.models import Category, Order, OrderItem, Product, Service, ShippingAddress
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.db.models import Prefetch
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import JsonResponse
import json

import datetime

# Directs the user to teh homepage


def home(request):
    return render(request, "products/index.html")


# It shows different waters sold
def waterSamples(request):
    categories = Category.objects.filter(name__startswith="Waters")

    page_num = request.GET.get("page")
    paginator = Paginator(categories, 3)
    try:
        categories = paginator.page(page_num)
    except PageNotAnInteger:
        categories = paginator.page(1)
    except EmptyPage:
        categores = paginator.page(paginator.num_pages)

    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartitems = order.get_cart_items
    else:
        items = []
        order = {' get_cart_total': 0, 'get_cart_items': 0}
        cartitems = order['get_cart_items']

    waters = Product.objects.all()

    context = {
        'categories': categories, 'waters': waters, 'cartitems': cartitems
    }

    return render(request, "products/waterSamples.html", context)


# Different Water Services
'''def waterServices(request):
    categories = Category.objects.filter(
        name__startswith="Services")
    page_num = request.GET.get("page")
    paginator = Paginator(categories, 3)
    try:
        categories = paginator.page(page_num)
    except PageNotAnInteger:
        categories = paginator.page(1)
    except EmptyPage:
        categores = paginator.page(paginator.num_pages)

    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartitems = order.get_cart_items
    else:
        items = []
        order = {' get_cart_total': 0, 'get_cart_items': 0}
        cartitems = order['get_cart_items']

    waterservices = Product.objects.all()
    action = waterservices['action']
    if action == 'highest':
        waterservices = Product.objects.all().order_by('price')
        print('highest')
    elif action == 'lowest':
        waterservices = Product.objects.all().order_by('-price')
        print('lowest')

    context = {
        'categories': categories, 'waterservicess': waterservices, 'cartitems': cartitems
    }
    return render(request, "products/waterServicesPage.html", context)'''


# Different water Products
def waterProducts(request):
    categories = Category.objects.filter(
        name__startswith="Products").order_by('name')
    page_num = request.GET.get("page")
    paginator = Paginator(categories, 3)
    try:
        categories = paginator.page(page_num)
    except PageNotAnInteger:
        categories = paginator.page(1)
    except EmptyPage:
        categories = paginator.page(paginator.num_pages)

    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartitems = order.get_cart_items
    else:
        items = []
        order = {' get_cart_total': 0, 'get_cart_items': 0}
        cartitems = order['get_cart_items']

    waters = Product.objects.all()
    context = {
        'categories': categories, 'waters': waters, 'cartitems': cartitems
    }
    return render(request, "products/WaterProductPage.html", context)


# Help page
def help(request):

    return render(request, 'products/help.html')

# About us page


def aboutUs(request):
    return render(request, 'products/aboutus.html')


def funAndGames(request):
    prod = Product.objects.in_bulk([1])
    print(prod)
    return render(request, 'products/waterfunpage.html')


# Displaying different brands
def brands(request):
    return render(request, 'products/brand.html')


# my Water services
def mywater(request):
    productss = Product.objects.all()[4: 8]
    products = Product.objects.all()[1:4]
    context = {
        'products': products,
        'products': productss
    }
    return render(request, 'products/mywater.html', context)


# showing the details of single products
def productDetail(request, pk):
    categories = Category.objects.all()
    eachProduct = Product.objects.get(id=pk)
    brand = eachProduct.brand
    thisbrand = Product.objects.prefetch_related('brand')
    print(thisbrand)
    print(brand)
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartitems = order.get_cart_items
    else:
        items = []
        order = {' get_cart_total': 0, 'get_cart_items': 0}
        cartitems = order['get_cart_items']

    context = {
        'cartitems': cartitems,
        'eachProduct': eachProduct,
        'categories': categories,

    }
    return render(request, 'products/ProductDetails.html', context)


# Search functionalities, implementation
def search(request):
    if request.method == "POST":
        search = request.POST['q']
        categories = Category.objects.filter(name__contains=search)
        product = Product.objects.filter(title__contains=search)
        if request.user.is_authenticated:
            customer = request.user
            order, created = Order.objects.get_or_create(
                customer=customer, complete=False)
            items = order.orderitem_set.all()
            cartitems = order.get_cart_items
        else:
            items = []
            order = {' get_cart_total': 0, 'get_cart_items': 0}
            cartitems = order['get_cart_items']
        context = {
            'search': search,
            'categories': categories,
            'product': product,
            'cartitems': cartitems
        }
        return render(request, "products/search.html", context)
    else:
        return render(request, "products/search.html", {})


@ login_required
@allowed_user(allowed_roles=['customer', 'admin'])
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()

        cartitems = order.get_cart_items
        # 'return redirect('purchaseOnDelivery')
    else:
        items = []
        order = {' get_cart_total': 0, 'get_cart_items': 0}
        cartitems = order['get_cart_items']
    context = {'items': items, 'order': order, 'cartitems': cartitems}
    return render(request, 'products/checkout.html', context)

# Customers cart


def userCart(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartitems = order.get_cart_items
    else:
        items = []
        order = {' get_cart_total': 0, 'get_cart_items': 0}
        cartitems = order['get_cart_items']
    context = {'items': items, 'order': order, 'cartitems': cartitems}
    return render(request, 'products/cart.html', context)


def updateItem(request):
    print('Data: is this', request.body)
    data = json.loads(request.body)
    productId = data['productId'] or data['eachProductId']
    action = data['action']
    print('Action', action)
    print('productId:', productId)

    customer = request.user
    product = Product.objects.get(id=productId)

    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)

    orderitem, created = OrderItem.objects.get_or_create(
        order=order, product=product)

    if action == 'remove':
        orderitem.quantity = (orderitem.quantity-1)
        print("Removed")

    elif action == 'remove-completely':
        orderitem.quantity = (orderitem.quantity == 0)
        print("Removed from cart")

    elif action == 'add':
        orderitem.quantity = (orderitem.quantity+1)
    orderitem.save()

    if orderitem.quantity <= 0:
        orderitem.delete()

    return JsonResponse('It was added', safe=False)


# Integrating the site with Mpesa and paypal payment methods3
def paymentmethods(request):
    return render(request, "products/payment.html")


# Last recap of Order processing
def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    print(data)
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        total = order.get_cart_totals
        order.transaction_id = transaction_id

        if total == order.get_cart_totals:
            order.complete = True
        order.save()
        if order.shipping == True:
            print("Wrong")
            ship = ShippingAddress(
                customer=customer,
                order=order,
                firstname=data['shipping']['firstname'],
                lastname=data['shipping']['lastname'],
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                zipcode=data['shipping']['zipcode']
            )
            ship.save(force_insert=True)
    else:
        print("User doesn't exist")
    print('Data:', request.body)
    return JsonResponse('Payment Submitted', safe=False)


# Dealing with Managers-Admin-
# Create, Update and Delete Categories, subcategories and Products
@login_required
@allowed_user(allowed_roles=['admin', 'staff'])
def showProduct(request):
    allproducts = Product.objects.all()
    number_of_products = Product.objects.all().count()
    context = {
        'allproducts': allproducts,
        'number_of_products': number_of_products

    }
    return render(request, 'products/Admin/modifyAllProducts.html', context)


# Manager add product
@login_required
@allowed_user(allowed_roles=['admin', 'staff'])
def addProduct(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('modifyAllProduct')
        else:
            form = ProductForm()
    context = {
        'form': form
    }
    return render(request, 'products/Admin/addProduct.html', context)

# Manager updating Product


@login_required
@allowed_user(allowed_roles=['admin', 'staff'])
def updateProduct(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('modifyAllProduct')
        else:
            form = ProductForm()
    context = {
        'form': form
    }
    return render(request, 'products/Admin/updateProduct.html', context)


# Manager deleting product
@login_required
@allowed_user(allowed_roles=['admin', 'staff'])
def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return redirect('modifyAllProduct')


# Manager accessing details of products
@login_required
@allowed_user(allowed_roles=['admin', 'staff'])
def modifySingleProduct(request, pk):
    eachProduct = Product.objects.get(id=pk)
    context = {
        'eachProduct': eachProduct}
    return render(request, 'products/Admin/modifySingleProduct.html', context)


# Managers adding a category
@login_required
@allowed_user(allowed_roles=['admin', 'staff'])
def addCategory(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('modifyAllProduct')
        else:
            form = CategoryForm()
    context = {
        'form': form
    }
    return render(request, 'products/Admin/addCategory.html', context)


# Managers adding a category
@login_required
@allowed_user(allowed_roles=['admin', 'staff'])
def addBrand(request):
    form = BrandsForm()
    if request.method == 'POST':
        form = BrandsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('modifyAllProduct')
        else:
            form = BrandsForm()
    context = {
        'form': form
    }
    return render(request, 'products/Admin/addBrand.html', context)


@login_required
@allowed_user(allowed_roles=['admin', 'staff'])
def creteOrder(request):
    form = orderForm()
    if request.method == 'POST':
        # pro = Product.objects.prefetch_related(
        # Prefetch('category', queryset=Category.objects.order_by('name')))
        pro = Product.objects.only('created_at').defer('title')
        print(pro)
        form = orderForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('home')
    context = {'form': form}
    return render(request, 'products/Admin/orderForm.html', context)


@login_required
@allowed_user(allowed_roles=['admin', 'staff'])
def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = orderForm(instance=order)
    if request.method == 'POST':
        print("mania ur sickening")
        form = orderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            redirect('home')

    context = {'form': form}
    return render(request, 'products/Admin/orderForm.html', context)


@login_required
@allowed_user(allowed_roles=['admin', 'staff'])
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        redirect('home')
    context = {'item': order}
    return render(request, 'products/Admin/deleteOrder.html', context)

# Single category


def singleCategoryProducts(request):
    category = Category.objects.all()
    product = Product.objects.all()
    context = {'category': category,
               'product': product}

    return render(request, 'products/singleCategory', context)


'''def getNumber(request):
    if request.user.is_authenticated:
        current_user = request.user
        number = current_user.username
        return number'''


@login_required
def Services(request):
    transaction_id = datetime.datetime.now().timestamp()
    form = serviceForm()
    c_form = constForm()
    p_form = plumbForm()
    cl_form = cleanForm()

    if request.user.is_authenticated:
        customer = request.user
        # service = Service.objects.all()
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)

        order.transaction_id = transaction_id
        if request.method == 'POST':
            form = serviceForm(request.POST)
            c_form = serviceForm(request.POST)
            cl_form = serviceForm(request.POST)
            p_form = serviceForm(request.POST)
            if 'house-help' in request.POST:
                if form.is_valid():
                    order.complete = True
                    order.save()
                    form.save()
                    Service.objects.filter(
                        location='Vihiga').update(order=order)
                else:
                    print("Invalid")

            elif 'clean' in request.POST:
                if c_form.is_valid():
                    order.complete = True
                    order.save()
                    c_form.save()
                    Service.objects.filter(
                        location='Vihiga').update(order=order)

            elif 'plumb' in request.POST:
                if cl_form.is_valid():
                    order.complete = True
                    order.save()
                    cl_form.save()
                    Service.objects.filter(
                        location='Vihiga').update(order=order)
                else:
                    print(cl_form.errors)

            elif 'construct' in request.POST:
                if p_form.is_valid():
                    order.complete = True
                    order.save()
                    p_form.save()
                    Service.objects.filter(
                        location='Vihiga').update(order=order)

            else:
                # print(p_form.errors)
                print(c_form.errors)
        else:
            form = serviceForm()
            c_form = constForm()
            p_form = plumbForm()
            cl_form = cleanForm()

    context = {'form': form, 'c_form': c_form,
               'cl_form': cl_form, 'p_form': p_form}
    return render(request, 'products/service.html', context)


# Admin viewing the Service Orders
def AdminService(request):
    househelps = Service.objects.filter(title__startswith='House')
    cleanings = Service.objects.filter(title__startswith='Cleaning')
    plumbings = Service.objects.filter(title__startswith='Plumbing')
    constructions = Service.objects.filter(title__startswith='Construction')
    context = {'househelps': househelps,
               'cleanings': cleanings,
               'plumbings': plumbings,
               'constructions': constructions}
    return render(request, 'products/Admin/serviceOrdered.html', context)


# Blogs of teh platforms, intergrate with teh blog code
def NewsWelfare(request):
    context = {}
    return render(request, 'products/FunNews/NewsWelfare.html', context)


def NewsLocal(request):
    context = {}
    return render(request, 'products/FunNews/NewsLocal.html', context)


def NewsInternational(request):
    context = {}
    return render(request, 'products/FunNews/NewsInternational.html', context)


# Allow user download variety of wallpaper related to water
def wallpapers(request):
    context = {}
    return render(request, 'products/FunNews/wallpapers.html', context)


# Games to be played
def ringsofwater(request):
    context = {}
    return render(request, 'products/FunNews/ringOfWater.html', context)


def waterfacts(request):
    context = {}
    return render(request, 'products/FunNews/waterFacts.html', context)
