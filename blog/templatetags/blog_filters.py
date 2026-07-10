from django import template

register = template.Library()


@register.simple_tag
def greeting(name):
    return f'Hola {name}! Bienvenido a MiblogFinal.'


@register.filter
def format_date(value):
    if not value:
        return ''
    return value.strftime('%d/%m/%Y')
