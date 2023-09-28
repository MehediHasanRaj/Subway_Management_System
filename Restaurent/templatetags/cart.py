import requests
from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product,cart):
    keys = cart.keys()
    for id in keys:
        if int(id)==product.id:
            return cart[id]
@register.filter(name='price_total')
def price_total(product,cart):
    keys = cart.keys()
    for id in keys:
        if int(id)==product.id:
            return round(float(cart[id]) * float(product.price),2)

@register.filter(name="total")
def total(products,cart):
    sum = 0
    for p in products:
        sum = sum + price_total(p,cart)
    return round(sum,2)