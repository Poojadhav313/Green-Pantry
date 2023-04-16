from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import *

from django.contrib.auth.hashers import make_password, check_password

# Create your views here.
def home(request):
  if(request.method == 'GET'):
    return render(request, 'store/home.html')
  else:
    name = request.POST.get('name')
    email = request.POST.get('email')
    msg = request.POST.get('msg')

    print(msg)
    review = Review(Cname = name, Cemail = email, Cmsg = msg)
    review.save()

  return render(request, 'store/home.html')


def store(request):
  if(request.method == 'GET'):
    cart = request.session.get('cart')
    if cart:
      pass
    else:
      request.session.cart = {}

    allProducts = Product.objects.all()
    content = {'products' : allProducts}
    return render(request, 'store/store.html', content)

  if(request.method == 'POST'):
    item = request.POST.get('productId') #getting id after clicking add_to_cart
    cart = request.session.get('cart')
    if cart:
      quantity = cart.get(item)
      if quantity:
        cart[item] = quantity + 1
      else: 
        cart[item] = 1
    else:
      cart = {}
      cart[item] = 1

    request.session['cart'] = cart
    print(request.session.get('cart'))

    return redirect('store_page')


def signup(request):
  if (request.method == 'GET'):
    return render(request, 'store/signup.html')
  else:
    #fetch values from form
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    password = request.POST.get('password')
    values = {
      'name': name,
      'email': email,
      'phone': phone,
    }

    error_msg = None
    customer = Customer(name = name, email = email, phone = phone, password = password)
      
    def specialChar(passs):
      for c in passs:
        if (c == '@' or c == '#' or c == '!' or c == '$'):
            return True
      return False

    #ughhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
    if customer.customerExists():
      error_msg = 'Email already registered!'
    elif not phone.isnumeric():
      error_msg = 'Phone number Invalid!'
    elif len(password) < 6:
      error_msg = 'Password too short!'
    elif not specialChar(password):
      error_msg = 'Password must contain at least 1 Special symbol!'
    elif not any(p.isdigit() for p in password):
      error_msg = 'Password must contain at least 1 numeric character!'
    elif not any(p.isalpha() for p in password):
      error_msg = 'Password must contain Alphabetic character!'





    if error_msg:
      content = {'error' : error_msg, 'values' : values}
      return render(request, 'store/signup.html', content)
    else:
      customer.password = make_password(customer.password)
      customer.register()
      return redirect('login_page') #in urls

 
def login(request):
  if request.method == 'GET':
    return render(request, 'store/login.html')
  else: #request == POST
    email = request.POST.get('email')
    password = request.POST.get('password')
    
    error_msg = None
    customer = Customer.getCustomerByEmail(email)
    
    if customer:
      if check_password(password, customer.password):
        request.session['customer'] = customer.id
        
        return redirect('store_page')  
      else:
        error_msg = 'Password Invalid!'

    else:
      error_msg = 'Email Invalid!'

    if error_msg:
      content = {'error' : error_msg, 'value_email' : email}
      return render(request, 'store/login.html', content)
    else:
      return redirect('store_page')

 
# def logout0(request):
#   if request.method == 'GET':
#     print("ooooooo")
#     return request(render, 'store/logout.html')
#   else:
#     return redirect('logout_page')


def logout(request):
  request.session.clear()
  return redirect('login_page')


def thanku(request):
  if request.method == 'POST':
    return render(request, 'store/thanku.html')
  return render(request, 'store/thanku.html')
  

def cart(request):
  content = {}
  try:
    if request.method == 'GET':
      cart = request.session.get('cart')
      if cart:
        ids = list(request.session.get('cart').keys())
        items = Product.getItemsById(ids)
        content = {'items' : items}
        return render(request, 'store/cart.html', content)
      else:
        cart = {}
        return render(request, 'store/emptyCart.html')
    else: 
      pass
  except:
    return render(request, 'store/cart.html', content)


def checkout0(request):
    #print('yolo')
    return redirect('checkout_page')


def checkout(request):
  if request.method == 'GET':
    customer = request.session.get('customer')
    cart = request.session.get('cart')
    items = Product.getItemsById(list(cart.keys()))
    context = {'items': items}
  else:
    customer = request.session.get('customer')
    cart = request.session.get('cart')
    items = Product.getItemsById(list(cart.keys()))
    context = {'items': items}
    Caddress = request.POST.get('add')
    Ccity = request.POST.get('city')
    Cstate = request.POST.get('state')
    Cpin = request.POST.get('pin')

    print(Caddress)
  # print(cart)
  # print(items)
  # print(customer)

    for item in items:
      order = Order(customer = Customer(id = customer), product = item, quantity = cart.get(str(item.id)), price = item.price, address = Caddress, city = Ccity, state = Cstate)
      order.save()
    # print(item, cart.get(str(item.id)),item.price, Caddress,Ccity,Cstate)

    request.session['cart'] = {}
  return render(request, 'store/checkout.html', context)


def orders(request):
  if request.method == 'GET':
    customer = request.session.get('customer')
    orderlist = Order.getOrders(customer)
    
    context = {'items' : orderlist}
  return render(request, 'store/orders.html', context)


def payment(request):
  return render(request, 'store/payment.html')


def aboutus(request):
  return render(request, 'store/aboutus.html')