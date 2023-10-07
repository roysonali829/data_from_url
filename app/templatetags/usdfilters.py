from django import template
register = template.Library()
def swap(value):
    return value.swapcase()

register.filter('swap',swap)