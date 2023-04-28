from django.contrib import admin
from .models import *


class AdminCustomer(admin.ModelAdmin):
  list_display = ['name', 'email']

class AdminProduct(admin.ModelAdmin):
  list_display = ['name', 'price']

class AdminOrder(admin.ModelAdmin):
  list_display = ['customer', 'price', 'date', 'status']

class AdminPayment(admin.ModelAdmin):
  list_display = ['customer', 'CardNo']

class AdminReview(admin.ModelAdmin):
  list_display = ['Cname', 'Cemail']

# Register your models here.
admin.site.register(Customer, AdminCustomer)
admin.site.register(Product, AdminProduct)
admin.site.register(Order, AdminOrder)
admin.site.register(Payment, AdminPayment)
admin.site.register(Review, AdminReview)
