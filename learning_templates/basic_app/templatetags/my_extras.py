from django import template

register = template.Library()

@register.filter(name='cut')
def cutoff(value,arg):
    return value.replace(arg,'')

# register.filter('cutoff',cutoff)
