from django.shortcuts import render, redirect
from .models import Customer, Product, Cart, OrderPlaced
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, UsernameField, PasswordChangeForm, \
    PasswordResetForm
from .forms import UserRegistrationForm, CustomerForm
from django.views import View
from django.contrib import messages
from django.contrib.auth import views as auth_view
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class ProductView(View):
    def get(self, request):
        topwear = Product.objects.filter(category="TW")
        bottomwear = Product.objects.filter(category='BW')
        electronic = Product.objects.filter(category='L')
        gadget = Product.objects.filter(category='M')
        return render(request, 'app/home.html',
                      {"topwear": topwear, "electronic": electronic, "gadgets": gadget, "bottomwear": bottomwear})


class ProductDetailView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        if request.user.is_authenticated:
            itemexist = Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()
            return render(request, 'app/productdetail.html', {"prod": product, 'itemexist': itemexist})
        return render(request, 'app/productdetail.html', {"prod": product})


@login_required
def add_to_cart(request):
    product_id = request.GET.get("prod_id")
    product = Product.objects.get(id=product_id)
    Cart(user=request.user, product=product).save()
    return redirect('showcart')


@login_required(login_url='login')
def PlusCart(request):
    if request.method == 'GET':
        prod_id = request.GET.get('prod_id')
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        amount = 0.0
        shipping_charge = 70.0
        total_amount = 0.0
        Carts = Cart.objects.filter(user=request.user)
        for p in Carts:
            amount += p.product.discounted_price * p.quantity
        total_amount = amount + shipping_charge
        data = {
            'amount': amount,
            'total_amount': total_amount,
            'quantity': c.quantity
        }
        print(data)
        return JsonResponse(data)


@login_required(login_url='login')
def MinusCart(request):
    if request.method == 'GET':
        prod_id = request.GET.get('prod_id')
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        if c.quantity > 1:
            c.quantity -= 1
        c.save()
        amount = 0.0
        shipping_charge = 70.0
        total_amount = 0.0
        Carts = Cart.objects.filter(user=request.user)
        for p in Carts:
            amount += (p.product.discounted_price) * p.quantity
        total_amount = amount + shipping_charge
        data = {
            'amount': amount,
            'total_amount': total_amount,
            'quantity': c.quantity
        }
        print(data)
        return JsonResponse(data)


@login_required
def RemoveCart(request):
    if request.method == 'GET':
        prod_id = request.GET.get('prod_id')
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        amount = 0.0
        shipping_charge = 70.0
        Carts = Cart.objects.filter(user=request.user)
        for p in Carts:
            amount += p.product.discounted_price * p.quantity
        total_amount = amount + shipping_charge
        data = {
            'amount': amount,
            'total_amount': total_amount,
        }
        return JsonResponse(data)


@login_required(login_url='login')
def ShowCart(request):
    Carts = Cart.objects.filter(user=request.user)
    if request.user.is_authenticated and Carts:
        amount = 0.0
        shipping_charge = 70.0
        total_amount = 0.0
        for p in Carts:
            amount += p.product.discounted_price
        total_amount = amount + shipping_charge
        return render(request, 'app/addtocart.html', {'carts': Carts, 'amount': amount, "total": total_amount})
    else:
        return render(request, 'app/emptycart.html')


def buy_now(request):
    return render(request, 'app/buynow.html')


@login_required
def address(request):
    data = Customer.objects.filter(user=request.user)
    return render(request, 'app/address.html', {'form': data, 'active': 'btn btn-primary'})


@login_required
def orders(request):
    data = OrderPlaced.objects.filter(user=request.user)
    return render(request, 'app/orders.html', {'data': data})


@login_required
def change_password(request):
    return render(request, 'app/changepassword.html')


def mobile(request, data=None):
    if data == None:
        result = Product.objects.filter(category="M")
    elif (data == "Apple" or data == 'samsung'):
        result = Product.objects.filter(category="M").filter(brand=data)
    elif data == 'below':
        result = Product.objects.filter(category="M").filter(discounted_price__lt=20000)

    elif data == 'above':
        result = Product.objects.filter(category="M").filter(discounted_price__gt=20000)

    return render(request, 'app/mobile.html', {'result': result})


def laptop(request, data=None):
    if data == None:
        result = Product.objects.filter(category="L")
    elif data == 'below':
        result = Product.objects.filter(category="L").filter(discounted_price__lt=30000)
    elif data == 'above':
        result = Product.objects.filter(category="L").filter(discounted_price__gt=30000)
    return render(request, 'app/laptops.html', {'rsult': result})


def topwear(request, data=None):
    if data == None:
        result = Product.objects.filter(category="TW")
    elif data == 'below':
        result = Product.objects.filter(category="TW").filter(discounted_price__lte=2000)
    elif data == 'above':
        result = Product.objects.filter(category="TW").filter(discounted_price__gt=2000)
    return render(request, 'app/topwear.html', {'rsult': result})


def bottomwear(request, data=None):
    if data == None:
        result = Product.objects.filter(category="BW")
    return render(request, 'app/bottomwear.html', {'rsult': result})


def bottomwear(request, data=None):
    if data == None:
        result = Product.objects.filter(category="BW")
    elif data == 'below':
        result = Product.objects.filter(category="BW").filter(discounted_price__lte=1000)
    elif data == 'above':
        result = Product.objects.filter(category="BW").filter(discounted_price__gt=1000)
    return render(request, 'app/bottomwear.html', {'rsult': result})


class UserCreationView(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'app/customerregistration.html', {'form': form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')


@login_required
def payment_done(request):
    customer = Customer.objects.get(id=request.GET.get('cust'))
    carts = Cart.objects.filter(user=request.user)
    for c in carts:
        OrderPlaced(user=request.user, customer=customer, product=c.product, quantity=c.quantity).save()
        c.delete()
    return redirect('orders')


@login_required
def checkout(request):
    cartinfo = Cart.objects.filter(user=request.user)
    Cust = Customer.objects.filter(user=request.user)
    amount = 0
    for cart in cartinfo:
        amount += cart.quantity * cart.product.discounted_price
    amount = amount + 70
    return render(request, 'app/checkout.html', {'Customer': Cust, 'cartinfo': cartinfo, 'amount': amount})


@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        form = CustomerForm()
        data = Customer.objects.all()
        return render(request, 'app/profile.html', {'form': form, 'active': 'btn btn-primary','data':data})

    def post(self, request):
        fmdata = CustomerForm(request.POST)
        if fmdata.is_valid():
            name = fmdata.cleaned_data['name']
            locality = fmdata.cleaned_data['locality']
            city = fmdata.cleaned_data['city']
            zipcode = fmdata.cleaned_data['zipcode']
            state = fmdata.cleaned_data['state']
            fm = Customer(user=request.user, name=name, city=city, locality=locality, zipcode=zipcode, state=state)
            fm.save()
            messages.success(request, 'Congratulation Your data is successfully posted')
            return render(request, 'app/profile.html', {'form': CustomerForm(), 'active': 'btn btn-primary'})
