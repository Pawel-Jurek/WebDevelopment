from django.template import Library

register = Library()

@register.inclusion_tag('tags/show_price.html')
def show_price(item):
    return {'total_price': round(item.dish.price * item.quantity, 3)}