from django.db import models
import datetime
from django.core.validators import RegexValidator


# Create your models here.
class Customer(models.Model):
  name = models.CharField(max_length=100, null=True)
  email = models.EmailField()
  phone = models.CharField(validators=[RegexValidator(r'^\d{0,10}$')], max_length=10, null=True)
  password = models.CharField(max_length=100, null=True)

  def __str__(self):
    return self.name

  def register(self):
    self.save()

  #@staticmethod
  def customerExists(self): #for sign up
    if Customer.objects.filter(email = self.email):
      return True
    return False

  @staticmethod
  def getCustomerByEmail(email): #for log in
    try:
      return Customer.objects.get(email = email)
    except:
      return False


class Product(models.Model):
  name = models.CharField(max_length=100)
  price  = models.IntegerField(default=0)
  description = models.CharField(max_length=200, default='', null=True, blank=True)
  image = models.ImageField(upload_to='upload/products/')

  def __str__(self):
    return self.name

  @staticmethod
  def getAllProducts(self): #---------------get_all_products------------
    return Product.objects.all()

  @staticmethod
  def getItemsById(ids):
    return Product.objects.filter(id__in = ids)


class Order(models.Model):
  customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  quantity = models.IntegerField(default=1)
  price  = models.IntegerField(default=0)
  address = models.CharField(max_length=200, null=True)
  city = models.CharField(max_length=200, null=True)
  state = models.CharField(max_length=200, null=True)
  date = models.DateField(default= datetime.datetime.today)
  status = models.BooleanField(default=False)

  @staticmethod
  def getOrders(cId):
    return Order.objects.filter(customer = cId).order_by('-date')


class Payment(models.Model):
  customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
  CardNo = models.CharField(validators=[RegexValidator(r'^\d{1,16}$')], max_length=16, null=True)
  CardCvv = models.CharField(validators=[RegexValidator(r'^\d{1,3}$')], max_length=3, null=True)
  CardYear = models.CharField(validators=[RegexValidator(r'^\d{1,4}$')], max_length=4, null=True)
  CardMonth = models.CharField(validators=[RegexValidator(r'^\d{1,2}$')], max_length=2, null=True)
  date = models.DateField(default= datetime.datetime.today)



class Review(models.Model):
  # customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
  Cname = models.CharField(max_length=100, null=True)
  Cemail = models.EmailField()
  Cmsg = models.CharField(max_length=500, null=True)
  date = models.DateField(default= datetime.datetime.today)


class Faq(models.Model):
  queNo = models.IntegerField(null=True)
  que = models.CharField(max_length=500, null=True)
  ans = models.CharField(max_length=500, null=True)

  def getfaq():
    return Faq.objects.filter().order_by('queNo')


class Discount(models.Model):
  DisName = models.CharField(max_length=50, null=True)
  DisPer = models.IntegerField(null=True)


class Supplier(models.Model):
  SupName = models.CharField(max_length=100, null=True)
  SupPhone = models.CharField(validators=[RegexValidator(r'^\d{0,10}$')], max_length=10, null=True)
  SupEmail = models.EmailField()
  SupAddress = models.CharField(max_length=100, null=True)

  def __str__(self):
    return self.SupName


class SupProduct(models.Model):
  supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True)
  product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
  SupDate = models.DateField(null=True)
  SupQuantity = models.IntegerField(null=True)


