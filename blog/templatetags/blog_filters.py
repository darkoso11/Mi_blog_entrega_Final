from django import template

register = template.Library()


@register.filter
def format_date(value):
    if not value:
        return ''
    return value.strftime('%d/%m/%Y')
