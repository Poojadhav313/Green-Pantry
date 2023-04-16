from django import template

register = template.Library()

@register.filter(name = 'is_in_cart')
def is_in_cart(item, cart):
  keys = cart.keys()
  for id in keys:
    if int(id) == item.id:
      return True

  return False

@register.filter(name = 'cart_quantity')
def cart_quantity(item, cart):
  keys = cart.keys()
  for id in keys:
    if int(id) == item.id:
      return cart.get(id)
  return 0

@register.filter(name = 'item_total')
def item_total(item, cart):
  return item.price * cart_quantity(item, cart)

@register.filter(name = 'price_total')
def price_total(items, cart):
  total = 0
  for price in items:
    total += item_total(price, cart)
  return total

@register.filter(name = 'cart_img')
def cart_img(item, cart):
  return item.image

@register.filter(name = 'mul')
def mul(m1,m2):
  return m1*m2