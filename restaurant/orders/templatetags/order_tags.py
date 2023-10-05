from django.template import Library

register = Library()

@register.inclusion_tag('tags/show_price.html')
def show_price(item):
    return {
        'total_price': f'{round(item.dish.price * item.quantity, 2):.2f}',
        'id': item.dish.pk
            }