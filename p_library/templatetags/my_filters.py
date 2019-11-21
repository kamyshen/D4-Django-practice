from django import template

register = template.Library()

@register.filter(name='range')
def custom_range(n):
    return range(1, n+1)