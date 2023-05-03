from django.contrib import admin
from .models import *


class AdminCustomer(admin.ModelAdmin):
  list_display = ['name', 'email']

class AdminProduct(admin.ModelAdmin):
  list_display = ['name','description', 'price']

class AdminOrder(admin.ModelAdmin):
  list_display = ['customer', 'price', 'date', 'status']

class AdminPayment(admin.ModelAdmin):
  list_display = ['customer', 'CardNo']

class AdminReview(admin.ModelAdmin):
  list_display = ['Cname', 'Cemail', 'date']

class AdminFaq(admin.ModelAdmin):
  list_display = ['queNo', 'que']

class AdminSupplier(admin.ModelAdmin):
  list_display = ['SupName', 'SupEmail', 'SupPhone']

class AdminSupProduct(admin.ModelAdmin):
  list_display = ['supplier', 'product', 'SupDate', 'SupQuantity']

class AdminDiscount(admin.ModelAdmin):
  list_display = ['DisName', 'DisPer']

# Register your models here.
admin.site.register(Customer, AdminCustomer)
admin.site.register(Product, AdminProduct)
admin.site.register(Order, AdminOrder)
admin.site.register(Payment, AdminPayment)
admin.site.register(Review, AdminReview)
admin.site.register(Faq, AdminFaq)
admin.site.register(Supplier, AdminSupplier)
admin.site.register(SupProduct, AdminSupProduct)
admin.site.register(Discount, AdminDiscount)
